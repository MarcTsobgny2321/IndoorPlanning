var map;
function myMap() {



  var pos = new google.maps.LatLng(-28.024, 140.887);
  var pos1 = new google.maps.LatLng(-27.024, 141.887);
  var pos2 = new google.maps.LatLng(-29.024, 142.887);

  mapType = ['HYBRID', 'SATELLITE', 'ROADMAP', 'TERRAIN'];
  var mapProp = {
    center: pos,
    zoom: 9,

    //Paramettres suplémentaires
    disableDefaultUI: true,
    panControl: true,
    zoomControl: true,
    mapTypeControl: true,
    scaleControl: true,
    streetViewControl: true,
    overviewMapControl: true,
    rotateControl: true,
    // mapTypeId: google.maps.MapTypeId.SATELLITE
  };
  map = new google.maps.Map(document.getElementById("googleMap"), mapProp);
  // alert('Déja affiché Suis je vraiment pris en compte????');

  var marker = new google.maps.Marker({
    position: pos,
    // icon: 'data:image/jpeg;base64,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',
  });

  marker.setMap(map);

  var myCity = new google.maps.Circle({
    center: pos,
    radius: 20000,
    strokeColor: "#0000FF",
    strokeOpacity: 0.8,
    strokeWeight: 2,
    fillColor: "#0000FF",
    fillOpacity: 0.4
  });
  myCity.setMap(map);



  var myTrip = [pos, pos1, pos2];
  var flightPath = new google.maps.Polyline({
    path: myTrip,
    strokeColor: "#0000FF",
    strokeOpacity: 0.8,
    strokeWeight: 2
  });

  flightPath.setMap(map);



  var infowindow = new google.maps.InfoWindow({
    content: "Mon site"
  });

  infowindow.open(map, marker);


  // Zoom to 9 when clicking on marker
  google.maps.event.addListener(marker, 'click', function () {
    map.setZoom(12);
    map.setCenter(marker.getPosition());
  });

  //Open infowindow when to click

  var infowindow = new google.maps.InfoWindow({
    content: "Caratéristiques du site \n Nom : \n id :"
  });

  google.maps.event.addListener(marker, 'click', function () {
    infowindow.open(map, marker);
  });



  /*The placeMarker() function places a marker where the user has clicked, and shows an infowindow with the latitudes and longitudes of the marker:
  */
  google.maps.event.addListener(map, 'click', function (event) {
    placeMarker(map, event.latLng);
  });

  function placeMarker(map, location) {
    var marker = new google.maps.Marker({
      position: location,
      map: map
    });
    var infowindow = new google.maps.InfoWindow({
      content: 'Latitude: ' + location.lat() +
        '<br>Longitude: ' + location.lng()
    });
    infowindow.open(map, marker);
  }









  infoWindow = new google.maps.InfoWindow();

  const locationButton = document.createElement("button");

  locationButton.textContent = "Pan to Current Location";
  locationButton.classList.add("custom-map-control-button");
  map.controls[google.maps.ControlPosition.TOP_CENTER].push(locationButton);
  locationButton.addEventListener("click", () => {
    // Try HTML5 geolocation.

    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        (position) => {
          const pos = {
            lat: position.coords.latitude,
            lng: position.coords.longitude,
          };

          infoWindow.setPosition(pos);
          infoWindow.setContent('Location found.<br> lat : ' + pos.lat + '<br>long :' + pos.lng);
          map.setZoom(18);
          map.setCenter(pos);
          var marker1 = new google.maps.Marker({
            position: pos,
          });

          marker1.setMap(map);
          infoWindow.open(map, marker1);

        },
        () => {
          handleLocationError(true, infoWindow, map.getCenter());
        }
      );
    } else {
      // Browser doesn't support Geolocation
      handleLocationError(false, infoWindow, map.getCenter());
    }
  });






  
  
  
} 

function placeMarker(map, location) {
  var marker = new google.maps.Marker({
    position: location,
    map: map
  });
  var infowindow = new google.maps.InfoWindow({
    content: 'Latitude: ' + location.lat() +
      '<br>Longitude: ' + location.lng()
  });
  infowindow.open(map, marker);
}


function searchLoc() {
  const lat = parseFloat($('#lat').val());
  const lng = parseFloat($('#lng').val());
  placeMarker(map, new google.maps.LatLng(lat, lng));

}

function placeMaker2(latlng) {
// console.log('type of latlng parameters :'+typeof(latlng));
placeMarker(map, new google.maps.LatLng( parseFloat(latlng[0]),parseFloat(latlng[1])));
}
