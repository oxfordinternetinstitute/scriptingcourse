'''<!DOCTYPE html>
<html>
  <head>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
    <meta charset="utf-8">
    <title>Simple markers</title>
    <style>
      html, body, #map-canvas {
        height: 100%;
        margin: 0px;
        padding: 0px
      }
    </style>
    <script src="https://maps.googleapis.com/maps/api/js?v=3.exp&sensor=false"></script>
    <script>
function initialize() {'''

  var myLatlng1 = new google.maps.LatLng(-25.363882,131.044922);
  var myLatlng2 = new google.maps.LatLng(-26.363882,132.044922);
  var myLatlng3 = new google.maps.LatLng(-25.363882,132.044922);
  
  var mapOptions = {
    zoom: 4,
    center: myLatlng1
  }
  var map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
'''
  var marker1 = new google.maps.Marker({
      position: myLatlng1,
      map: map,
      title: 'Hello bop World!'
  });

  var marker2 = new google.maps.Marker({
      position: myLatlng2,
      map: map,
      title: 'Hello burp World!'
  });

  var marker3 = new google.maps.Marker({
      position: myLatlng3,
      map: map,
      title: 'Hello beep World!'
  });

var contentString = '<div>Hello 😂 world</div>';

  var infowindow = new google.maps.InfoWindow({
      content: contentString
  });

    google.maps.event.addListener(marker1, 'click', function() {
    infowindow.open(map,marker1);
  });
}

google.maps.event.addDomListener(window, 'load', initialize);

    </script>
  </head>
  <body>
    <div id="map-canvas"></div>
  </body>
</html>