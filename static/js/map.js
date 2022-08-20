'use strict';

// value-hoisting
function initMap() {

  const spokaneCoords = {
    lat: 47.65887479796297,
    lng: -117.42540975144257,
  };

  const map = new google.maps.Map(document.querySelector('#map'), {
    center: spokaneCoords,
    zoom: 10,
    mapTypeId: google.maps.MapTypeId.TERRAIN,
  });

  const routeInfo = new google.maps.InfoWindow();

  // retrieve routes with AJAX
  fetch('/api/routes')
    .then((response) => response.json())
    .then((routes) => {
      for (const route of routes) {
        // define content of the infoWindow
        const routeInfoContent = `hi
        `;

        const routeMarker = new google.maps.Marker({
          position: {
            lat: route.latitude,
            lng: route.longitude,
          },
          title: `Route Name: ${route.routeName}`,
          icon: {
            url: '/static/img/marker.png',
            scaledSize: new google.maps.Size(30, 30),
          },
          map,
        });

        routeMarker.addListener('click', () => {
          routeInfo.close();
          routeInfo.setContent(routeInfoContent);
          routeInfo.open(map, routeMarker);
        });
      }
    })
    .catch(() => {
      alert(`
      uh oh
    `);
    });
}