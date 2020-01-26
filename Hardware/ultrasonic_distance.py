#Libraries
import RPi.GPIO as GPIO
import time
import pymongo
##import getpass
import datetime
from collections import OrderedDict

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
    
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance

def push(flag):
    dt = datetime.datetime.today()
    seatDocument = OrderedDict([
        ("seatNo", 1),
        ("year", int(dt.strftime("%Y"))),
        ("month", int(dt.strftime("%m"))),
        ("day", int(dt.strftime("%d"))),
        ("dayOfWeek", int(dt.strftime("%w"))),
        ("hour", int(dt.strftime("%H"))),
        ("min", int(dt.strftime("%M"))),
        ("available", int(not flag)),
    ])
    seats.insert_one(seatDocument)
    print("Push Successful")
    return 0

##un = input("Enter username: ")
##pw = getpass.getpass(prompt="Enter password: ")

client = pymongo.MongoClient("mongodb+srv://ADMIN:admin@library-seat-tracker-fvhnk.azure.mongodb.net/gettingStarted?retryWrites=true&w=majority")
db = client.seatsAvailable
seats = db.seats

if __name__ == '__main__':
    try:
        isThere = 0
        while True:
            counter = 0
            for j in range(30):
                dist = distance()
                if (dist <= 100):
                    counter+=1
##                print ("Measured Distance = %.1f cm" % dist)
                time.sleep(0.1)
            if (counter >= 2 and isThere == 1):
                print("Still here...")
            elif(counter >= 2 and isThere == 0):
                isThere = 1
                print("Detected!")
                push(isThere)
            elif(counter < 2 and isThere == 1):
                isThere = 0
                print("Gone!")
                push(isThere)
            else:
                print("Nothing...")

 
    # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
