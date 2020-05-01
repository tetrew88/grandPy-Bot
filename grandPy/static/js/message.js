const chatZone = document.getElementById('conversation_screen');

function post_message(senderName, message)
{
	const chatZone = document.getElementById('conversation_screen');

	const bubbleText = document.createElement('li');

	bubbleText.classList.add("bubble_text");

	if(senderName == "GrandPy")
	{
		bubbleText.classList.add("start_allign");	
	}
	else
	{
		bubbleText.classList.add("end_allign");
		bubbleText.style.backgroundColor = "green";
	}

	const header = document.createElement('p');

	header.classList.add("messageHeader");
	header.textContent = senderName + ":";


	const content = document.createElement('p');

	content.classList.add("message");
	content.textContent  = message;

	bubbleText.appendChild(header);
	bubbleText.appendChild(content);

	chatZone.appendChild(bubbleText);

	chatZone.scrollTop = chatZone.scrollHeight;
}

function collect_message()
{
	let grandPy = new GrandPy();

	chatPicture = document.getElementById("chat_picture");

	const userInput = document.getElementById("userText");

	chatPicture.src = "static/images/loading.jpeg";

	let text = userInput.value;

	if (text == "")
	{
		alert("Entrer une question");
	}

	else
	{
		post_message("vous", text);

		fetch('/ask',
		{
			method: "POST",
			body: new FormData(document.getElementById("userInput"))
		})
		.then(response => {
			return response.json();
		})
	    .then(data => {
	    	console.log(data)
	    	
	    	if(data != false)
	    	{
	    		chatPicture.src = "static/images/succes.jpeg";
	    		
	    		let place = new Place(data["placeName"], 
	    			data["address"], 
	    			data["informations"], 
	    			data["latitude"], 
	    			data["longitude"]);

	        	post_response(place);
	        }

	        else
	        {
	        	post_message("GrandPy", "Désoler une erreur c'est produite :/");
	        }
	    })
	    .catch(error => {
	        console.error(error);
	    });
	}
}

function post_response(place)
{
	let grandPy = new GrandPy();
		
	const bubbleText = document.createElement('li');
	bubbleText.classList.add("bubble_text");
	bubbleText.classList.add("start_allign");
		
	const content = document.createElement('ul');

	const header = document.createElement('li');
	header.textContent = ("GrandPy:");

	const succes = document.createElement('li');
	succes.textContent = "    " + grandPy.succesResponses[aleatory(grandPy.succesResponses.length)];

	const adress = document.createElement('li');
	adress.textContent = 'adresse: ' + place.address;

	const informations = document.createElement('ul');
	informations.textContent = grandPy.informations[aleatory(grandPy.informations.length)];

	const informationsContent = document.createElement('li');
	informationsContent.textContent = place.informations;

	const mapIntroduction = document.createElement('li');
	mapIntroduction.textContent = grandPy.mapIntroductions[aleatory(grandPy.mapIntroductions.length)];


	informations.appendChild(informationsContent);

	content.appendChild(header);
	content.appendChild(succes);
	content.appendChild(adress);
	content.appendChild(informations);
	content.appendChild(informationsContent);
	content.appendChild(mapIntroduction);
	content.appendChild(map);

	bubbleText.appendChild(content);

	chatZone.appendChild(bubbleText);

	map = document.getElementById('map');
	map.style.width = '600px';
	map.style.height = '400px';

	initMap(place);

	chatZone.scrollTop = chatZone.scrollHeight;
}