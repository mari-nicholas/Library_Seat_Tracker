var express= require("express"), app = express(), http=require("http").Server(app).listen(3000);

app.use("/css", express.static("./css"))
app.use("/img",express.static("./img"))
app.use("/js", express.static("./js"))
app.use("/data", express.static("./data"))
app.get("/", function(req,res){
	res.sendFile(__dirname+"/home.html");
})
app.get("/home", function(req,res){
	res.sendFile(__dirname+"/home.html");
})
app.get("/page1", function(req,res){
	res.sendFile(__dirname+"/page1.html");
})
app.get("/page2", function(req,res){
	res.sendFile(__dirname+"/page2.html");
})
app.get("/page3", function(req,res){
	res.sendFile(__dirname+"/page3.html");
})

function queryData() {
	//console.log("Test1");

	const MongoClient = require('mongodb').MongoClient;
	var url = "mongodb+srv://user:user@library-seat-tracker-fvhnk.azure.mongodb.net/test?retryWrites=true&w=majority";
	const fs = require('fs');


	MongoClient.connect(url, function(err, db) {
	  if (err) throw err;
	  var mydb = db.db("seatsAvailable");
	  var query = { 
				  $group:
					{
						_id: "$seatNo",
						lastState: { $last: "$available" }
					}
				};
	  mydb.collection("seats").aggregate([query]).toArray(function(err, result) {
	    if (err) throw err;
	    //console.log(result);
	    //console.log(JSON.stringify(result));
	    fs.writeFileSync('./data/data.json', JSON.stringify(result));
	    console.log("Loop");
	    db.close();
	  });
	});


}

setInterval(queryData, 15000);