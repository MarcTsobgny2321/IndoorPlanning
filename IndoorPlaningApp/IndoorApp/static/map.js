
var map;
class mm {
  constructor(lat, lng) {
    this.lat = lng;
    this.lng = lng
  }
}
function myMap() {



  var pos = new google.maps.LatLng(-28.024, 140.887);
  var pos1 = new google.maps.LatLng(-27.024, 141.887);
  var pos2 = new google.maps.LatLng(-29.024, 142.887);

  mapType = ['HYBRID', 'SATELLITE', 'ROADMAP', 'TERRAIN'];
  var mapProp = {
    center: pos,
    zoom: 9,

    //Paramettres suplémentaires
    disableDefaultUI: false,
    // panControl: true,
    // zoomControl: true,
    // mapTypeControl: true,
    // scaleControl: true,
    // streetViewControl: true,
    // overviewMapControl: true,
    // rotateControl: true,
    // mapTypeId: google.maps.MapTypeId.SATELLITE
  };
  map = new google.maps.Map(document.getElementById("googleMap"), mapProp);
  // alert('Déja affiché Suis je vraiment pris en compte????');

  var marker = new google.maps.Marker({
    position: pos,
    // icon: 'data:image/jpeg;base64,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',
    icon: 'data:image/png;base64,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'
  });

  marker.setMap(map);

  // var myCity = new google.maps.Circle({
  //   center: pos,
  //   radius: 20000,
  //   strokeColor: "#0000FF",
  //   strokeOpacity: 0.8,
  //   strokeWeight: 2,
  //   fillColor: "#0000FF",
  //   fillOpacity: 0.4
  // });
  // myCity.setMap(map);



  // var myTrip = [pos, pos1, pos2];
  // var flightPath = new google.maps.Polyline({
  //   path: myTrip,
  //   strokeColor: "#0000FF",
  //   strokeOpacity: 0.8,
  //   strokeWeight: 2
  // });

  // flightPath.setMap(map);



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
  // google.maps.event.addListener(map, 'click', function (event) {
  //   placeMarker(map, event.latLng);
  // });

  function placeMarker(map, location) {
    var marker = new google.maps.Marker({
      position: location,
      map: map,
      icon: 'data:image/png;base64,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'
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
  const icon = {
    url: "data:image/png;base64,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",
    scaledSize: new google.maps.Size(30, 30), // scaled size
    origin: new google.maps.Point(0, 0), // origin
    anchor: new google.maps.Point(0, 0) // anchor
  };

  var marker = new google.maps.Marker({
    position: location,
    map: map,
    icon: icon
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


function placeMarkerT(map, location, CI, Az) {




  const icon = {
   
    rotation: Az,
    path: "M7.247 11.14 2.451 5.658C1.885 5.013 2.345 4 3.204 4h9.592a1 1 0 0 1 .753 1.659l-4.796 5.48a1 1 0 0 1-1.506 0z",
    fillColor: "blue",
    fillOpacity: 0.9,
    strokeWeight: 0,
    scale: 2,
    anchor: new google.maps.Point(location.lat(), location.lng()),

  };


  var rotationAngle = Az;



  var marker = new google.maps.Marker({
    position: location,
    map: map,
    icon: icon
  });

  var infowindow = new google.maps.InfoWindow({
    content:
      'CI : ' + CI
      + '<br>Latitude: ' + location.lat() +
      '<br>Longitude: ' + location.lng() +
      '<br> Azimuth : ' + Az
  });

  marker.set
  marker.setMap(map);

  // var myCity = new google.maps.Circle({
  //   center: location,
  //   radius: 20000,
  //   strokeColor: "#0000FF",
  //   strokeOpacity: 0.8,
  //   strokeWeight: 2,
  //   fillColor: "#0000FF",
  //   fillOpacity: 0.4
  // });

  // myCity.setMap(map);



  google.maps.event.addListener(marker, 'click', function () {
    infowindow.open(map, marker);
  });


  infowindow.open(map, marker);
}




function placeMarkerM(map, location, infosWinText) {




  const icon = {
    url: "https://www.svgrepo.com/show/106230/antenna.svg",
    fillColor: "blue",
    fillOpacity: 0.9,
    strokeWeight: 0,
    scale: 4,
    anchor: new google.maps.Point(location.lat(), location.lng()),
    scaledSize: new google.maps.Size(30, 30), // scaled size
    origin: new google.maps.Point(0, 0), // origin
    // anchor: new google.maps.Point(0, 0), // anchor

  };

  var marker = new google.maps.Marker({
    position: location,
    map: map,
    icon: icon
  });

  var infowindow = new google.maps.InfoWindow({
    content:
      '<br>Latitude: ' + location.lat() +
      '<br>Longitude: ' + location.lng() +
      '<br> infos : ' + infosWinText
  });

  marker.set
  marker.setMap(map);
  google.maps.event.addListener(marker, 'click', function () {
    infowindow.open(map, marker);
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
  placeMarkerT(map, new google.maps.LatLng(parseFloat(latlng[1]), parseFloat(latlng[0])), latlng[2], parseFloat(latlng[3]));
}



function placeMaker3(lat, lng, HTMLText, angle, latM, lngM) {
  var tag = new google.maps.LatLng(parseFloat(lat), parseFloat(lng));
  placeMarkerM(map, tag, "Site Taged : <br>" + HTMLText);

  var my = new google.maps.LatLng(parseFloat(latM), parseFloat(lngM));
  placeMarkerM(map, my, "My position <br> Angle: " + angle);
  var myTrip = [tag, my];
  var flightPath = new google.maps.Polyline({
    path: myTrip,
    strokeColor: "#0000FF",
    strokeOpacity: 0.8,
    strokeWeight: 2
  });

  flightPath.setMap(map);


  map.setCenter(tag);
  map.setZoom(13);
}




function getCurrentLocation() {
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


}








