function al() {
    alert('function called');
  
    const lat = parseFloat($('#lat').val());
    const lng = parseFloat($('#lng').val());
    location = new google.maps.LatLng(lat, lng);
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
  