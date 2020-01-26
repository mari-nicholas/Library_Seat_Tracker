// const jsdom = require("jsdom");
// const { JSDOM } = jsdom;

// global.document = new JSDOM("home.html").window.document;

// var indicators = document.getElementsByClassName('occupied');

// var heading = document.getElementById('test');
// heading.innerHTML = 'Hello world!';
function queryData() {

	console.log("Test1");

	var MongoClient = require('mongodb').MongoClient;
	var url = "mongodb+srv://user:user@library-seat-tracker-fvhnk.azure.mongodb.net/test?retryWrites=true&w=majority";

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
	  mydb.collection("seats").aggregate(query).toArray(function(err, result) {
	    if (err) throw err;
	    console.log(result);
	    db.close();
	  });
	});

// 	const client = new MongoClient(url, { useNewUrlParser: true });

// 	client.connect(err => {
// 	const collection = client.db("seatsAvailable").collection("seats");
// 	const query = { 
// 				  $group:
// 					{
// 						_id: "$seatNo",
// 						lastState: { $last: "$available" }
// 					}
// 			};
// 	(async () => {
// 		try {
// 			let arr = await collection.aggregate([query])
// 			console.log(arr);
// 		} catch (err) {
// 			console.log("Fuck");
// 		}
// 	})();

// 	// if(arr[0]["available"] === 1) {
// 	// 	indicators[0].style.fill = rgb(0,255,0);
// 	// } else {
// 	// 	indicators[0].style.fill = rgb(255,0,0);
// 	// }

// 	client.close();
// 	});
}

queryData();
