var APPID = "f5069abcfd0981b52d3b633cb1033c5a";
var temp;
var loc;
var icon;
var humidity;
var wind;
var direction;


function updateByCity(city){
    var url = "http://api.openweathermap.org/data/2.5/weather?" +
        "q=" + city + ',IE' +
        "&APPID=" + APPID + "&units=metric";
    sendRequest(url);
}

function sendRequest(url){
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function(){
        if (xmlhttp.readyState == 4 && xmlhttp.status ==200){
            var data = JSON.parse(xmlhttp.responseText);
            var weather = {};
            weather.icon = data.weather[0].id;
            weather.humidity = data.main.humidity;
            weather.wind = data.wind.speed;
            weather.direction = data.wind.deg;
            weather.loc = data.name;
            weather.temp = data.main.temp;
            update(weather);
        }
    };
    xmlhttp.open("GET", url, true);
    xmlhttp.send();
}

function update(weather){
    wind.innerHTML = weather.wind;
    direction.innerHTML = weather.direction;
    humidity.innerHTML = weather.humidity;
    loc.innerHTML = weather.loc;
    temp.innerHTML = weather.temp;
    icon.src = "static/images/" + weather.icon + ".png";

}

window.onload = function(){
    temp = document.getElementById("temperature");
    loc = document.getElementById("location");
    icon = document.getElementById("icon");
    humidity = document.getElementById("humidity");
    wind = document.getElementById("wind");
    direction = document.getElementById("direction");

    updateByCity("Kenmare");
}