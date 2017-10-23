var c = function(position){
    var lat = position.coords.latitude,
        long = position.coords.longitude,
        coords = lat + ', ' + long;

    // document.getElementById('google_map').setAttribute('src', 'https://www.google.ie/maps/embed?' + coords + ',15z/data=!4m2!7m1!2e1?hl=en');
     document.getElementById('google_map').setAttribute('src', 'https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d9521.012513439806!2d' + long + '!3d'+ lat + '!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e0!3m2!1sen!2sie!4v1508788125467');

}

document.getElementById('get_location').onclick = function(){
    navigator.geolocation.getCurrentPosition(c);
    return false;
}