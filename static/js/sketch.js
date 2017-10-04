var weather;

var api = 'http://api.openweathermap.org/data/2.5/weather?q=';
var city = 'Kenmare';
var apiKey = '&APPID=f5069abcfd0981b52d3b633cb1033c5a';
var units = '&units=metrics';

function setup() {
    createCanvas(400, 200);
    var url = api + city + apiKey + units;
loadJSON(url, gotData);
}

function gotData(data){
weather = date;
}

function draw(){
    background(0);
    if (weather) {
        var temp = waether.main.temp;
        var icon = weather.main.icon;
        eclipse(100,100, temp, temp);
        eclipse(300,100, icon, icon);
    }
}