function main()
{
	chat = true;

	let grandPy = new GrandPy();

	grandPy.say_hello();
}


function initMap(place)
{
	// Créer l'objet "map" et l'insèrer dans l'élément HTML qui a l'ID "map"
	let map = new google.maps.Map(document.getElementById("map"),
	{
		// Nous plaçons le centre de la carte avec les coordonnées ci-dessus
		center: {lat: place.latitude, lng: place.longitude}, 
		// Nous définissons le zoom par défaut
		zoom: 16
	});

	var marker = new google.maps.Marker(
	{
		// Nous définissons sa position (syntaxe json)
		position: {lat: place.latitude, lng: place.longitude},
		// Nous définissons à quelle carte il est ajouté
		map: map
	});

}

main()