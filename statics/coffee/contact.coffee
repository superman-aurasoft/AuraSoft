jQuery ->
    if google?
        location = new google.maps.LatLng(37.5069481, 127.0529865)
        mapOptions =
            center: location
            zoom: 16
            mapTypeId: google.maps.MapTypeId.ROADMAP
            mapTypeControl: false
            scaleControl: false
            panControl: false
            zoomControl: true
            zoomControlOptions:
                style: google.maps.ZoomControlStyle.SMALL
          
        map = new google.maps.Map document.getElementById("mapcanvas"), mapOptions;
        marker = new google.maps.Marker
            position: location,
            map: map,
            title:"AURASOFT"
