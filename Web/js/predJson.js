function predJson() {
    var path = 'https://samm82.pythonanywhere.com/api'
    var http = new XMLHttpRequest();
    http.open('GET', url);
    http.responseType= 'text';
    // http.onload = function() {
    //   data = http.response;
    //   console.log(data);
    // };
    http.onreadystatechange = function(){
        if (http.readyState==4 && http.status == 200){
            data=http.responseText;
            console.log(data);
            var yes = document.getElementById("prediction").innerHTML;
            console.log(yes)
            yes = data;

        }
    }
    http.send();
}

predJson();