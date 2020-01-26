var express = require('express');
var app = express();

app.set('views', __dirname + '/views');


app.get('/', function(req, res){
  res.render('home.html', {
        title: 'Home',
    nav: ['1','2','3'] 
  });
});

app.get('/1', function(req, res){
  res.render('page1.html', {
        title: 'My Site',
    nav: ['1','2','3'] 
  });
});

app.get('/2', function(req, res){
  res.render('page2.html', {
    title: 'About',
     nav: ['1','2','3'] 
  });
});

app.get('/con3tact', function(req, res){
  res.render('page3.html', {
    title: 'Contact',
     nav: ['1','2','3'] 
  });
});


app.listen(3000);