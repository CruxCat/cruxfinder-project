'use strict';

// We use a function declaration for initMap because we actually *do* need
// to rely on value-hoisting in this circumstance.
function initMap() {
  const spokaneCoords = {
    lat: 47.65887479796297,
    lng: -117.42540975144257,
  };

  const basicMap = new google.maps.Map(document.querySelector('#map'), {
    center: spokaneCoords,
    zoom: 11,
  });

  const spokaneMarker = new google.maps.Marker({
    position: spokaneCoords,
    title: 'Spokane',
    map: basicMap,
  });

  spokaneMarker.addListener('click', () => {
    alert('Hi!');
  });

  const spokaneInfo = new google.maps.InfoWindow({
    content: '<h1>Spokane, WA</h1>',
  });

  spokaneInfo.open(basicMap, spokaneMarker);

  const locations = [
    {
      name: 'A Peaceful Transition',
      coords: {
        lat: 47.57852,
        lng: -117.28617,
      },
    },
    {
      name: 'Humpty Dumpty',
      coords: {
        lat: 47.64739,
        lng: -117.41954,
      },
    },
    {
      name: 'The Little Engine That Could',
      coords: {
        lat: 47.64739,
        lng: -117.41954,
      },
    },
    {
      name: 'Wallflower',
      coords: {
        lat: 47.701040,
        lng: -116.962860,
      },
    },
    {
      name: 'The Last of the Summer Wine',
      coords: {
        lat: 47.703930,
        lng: -116.963130,
      },
    },
    {
      name: 'Nebula',
      coords: {
        lat: 47.83965,
        lng: -117.75275,
      },
    },
    {
      name: 'Mid-Life Crisis',
      coords: {
        lat: -117.725,
        lng: 47.8356,
      },
    },
    {
      name: 'Invictus',
      coords: {
        lat: -117.28707,
        lng: 47.71088,
      },
    },
  ];

  const markers = [];
  for (const location of locations) {
    markers.push(
      new google.maps.Marker({
        position: location.coords,
        title: location.name,
        map: basicMap,
        icon: {
          // custom icon
          url: '/static/img/marker.png',
          scaledSize: {
            width: 30,
            height: 30,
          },
        },
      }),
    );
  }

  for (const marker of markers) {
    const markerInfo = `
      <h1>${marker.title}</h1>
      <p>
        Located at: <code>${marker.position.lat()}</code>,
        <code>${marker.position.lng()}</code>
      </p>
    `;

    const infoWindow = new google.maps.InfoWindow({
      content: markerInfo,
      maxWidth: 200,
    });

    marker.addListener('click', () => {
      infoWindow.open(basicMap, marker);
    });
  }
}
