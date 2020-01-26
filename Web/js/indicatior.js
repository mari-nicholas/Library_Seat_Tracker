//console.log("Test1");

// const MongoClient = require('mongodb').MongoClient;
// const url = "mongodb+srv://user:user@library-seat-tracker-fvhnk.azure.mongodb.net/test?retryWrites=true&w=majority";
// const client = new MongoClient(url, { useNewUrlParser: true });

// const jsdom = require("jsdom");
// const { JSDOM } = jsdom;

// global.document = new JSDOM("home.html").window.document;

var indicators = document.getElementsByClassName('occupied');

var heading = document.getElementById('test');
heading.innerHTML = 'Hello world!';

// client.connect(err => {
//   const collection = client.db("seatsAvailable").collection("seats");
//   var query = {
//   				_id: "$seatNo",
//   				lastState: { $last: "$available" }
// 			};
//   var arr = collection.find(query).toArray(function(err, result) {
//     if (err) throw err;
//     console.log(result);
//     db.close();
//   });

//   if(arr[0]["available"] === 1) {
//   	indicators[0].style.fill = rgb(0,255,0);
//   } else {
//   	indicators[0].style.fill = rgb(255,0,0);
//   }

//   client.close();
// });