var express= require("express"), app = express(), http=require("http").Server(app).listen(3000);

app.use("/css", express.static("./css"))
app.use("/img",express.static("./img"))
console.log("Server started at port 80")
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
