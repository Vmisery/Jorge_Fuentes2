const navToggle = document.querySelector(".nav-toggle");
const navMenu = document.querySelector(".nav-menu");
let map;

function initMap() {
   map = new google.maps.Map(document.getElementById('map'), {
 center: {lat: -33.511496, lng: -70.752689},
     zoom: 13,
   });
   var marker = new google.maps.Marker({
     position: {lat: -33.511496, lng: -70.752689},
     map: map,
title: 'Ground Zero'
   });
 }

 
navToggle.addEventListener("click", () => {
    navMenu.classList.toggle("nav-menu_visible");

    if (navMenu.classList.contains("nav-menu_visible")) {
        navToggle.setAttribute("aria-label", "Cerrar Menú");
    } else {
        navToggle.setAttribute("aria-label", "Abrir menú");
    }
});


