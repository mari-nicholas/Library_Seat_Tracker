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
				var temp = document.getElementsByClassName("occupied");
				for (var i = 0; i < temp.length; i++) {
					if(obj[i]["lastState"] === 1){
						temp[i].style.fill="green";	
						console.log(i, "green");
					} else if(obj[i]["lastState"] === 0) {
						temp[i].style.fill="red";
						console.log(i, "red");
					}
					else{

					}
				}	
		        });
	          fileReader.readAsText(file);
	      } 
	    }
	    xhr.send();
	})();
}

setInterval(readJson, 5000);
