function readJson() {
	(async () => {
		var path = '../data/data.json'
		var xhr = new XMLHttpRequest();
	    xhr.open('GET', path, true);
	    xhr.responseType = 'blob';
	    xhr.onload = function(e) { 
	      if (this.status == 200) {
	          var file = new File([this.response], 'temp');
	          var fileReader = new FileReader();
	          fileReader.addEventListener('load', function(){
	          	//console.log(fileReader.result);
				var obj = JSON.parse(fileReader.result);
				if(obj[0]["lastState"] === 1){
					document.getElementsByClassName("occupied")[0].style.fill="green";	
					console.log("green");
				} else {
					document.getElementsByClassName("occupied")[0].style.fill="red";
					console.log("red");
				}	
		        });
	          fileReader.readAsText(file);
	      } 
	    }
	    xhr.send();
	})();
}

setInterval(readJson, 15000);
