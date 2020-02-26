function main()
{
	chat = true;

	let grandPy = new GrandPy();

	grandPy.say_hello;
}


function initMap(place)
{
	// Créer l'objet "map" et l'insèrer dans l'élément HTML qui a l'ID "map"
	let map = new google.maps.Map(document.getElementsByClassName("map"),
	{
		// Nous plaçons le centre de la carte avec les coordonnées ci-dessus
		center: new google.maps.LatLng(place.latitude, place.longitude), 
		// Nous définissons le zoom par défaut
		zoom: 11, 
		// Nous définissons le type de carte (ici carte routière)
		mapTypeId: google.maps.MapTypeId.ROADMAP, 
		// Nous activons les options de contrôle de la carte (plan, satellite...)
		mapTypeControl: true,
		// Nous désactivons la roulette de souris
		scrollwheel: false, 
		mapTypeControlOptions:
		{
			// Cette option sert à définir comment les options se placent
			style: google.maps.MapTypeControlStyle.HORIZONTAL_BAR 
		},
		// Activation des options de navigation dans la carte (zoom...)
		navigationControl: true, 
		navigationControlOptions:
		{
			// Comment ces options doivent-elles s'afficher
			style: google.maps.NavigationControlStyle.ZOOM_PAN 
		}
	});

}

main()