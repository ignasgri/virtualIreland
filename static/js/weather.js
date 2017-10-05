var APPID = "f5069abcfd0981b52d3b633cb1033c5a";
var temp;
var loc;
var icon;
var humidity;
var wind;
var direction;

function updateByCity(city){
    
}

function update(weather){
    wind.innerHTML = weather.wind;
    direction.innerHTML = weather.direction;
    humidity.innerHTML = weather.humidity;
    loc.innerHTML = weather.loc;
    temp.innerHTML = weather.temp;
    icon.src = "static/images" + weather.icon + ".png";
}

window.onload = function(){
    temp = document.getElementById("temperature");
    loc = document.getElementById("location");
    icon = document.getElementById("icon");
    humidity = document.getElementById("humidity");
    wind = document.getElementById("wind");
    direction = document.getElementById("direction");

    var weather = {};
    weather.wind = 3.5;
    weather.direction = "N";
    weather.humidity = 35;
    weather.loc = "kenmare";
    weather.temp = "20";
    weather.icon = "sunny";

    update(weather);
}