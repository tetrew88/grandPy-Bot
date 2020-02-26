function post_message(senderName, message)
{
	const chatZone = document.getElementById('conversation_screen');

	const bubbleText = document.createElement('li');

	bubbleText.classList.add("bubble_text");

	if(senderName == "grandPy")
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
	const userInput = document.getElementById("userText");

	let text = userInput.value;

	if(text == "")
	{
		alert("Entrer une question");
	}
	else
	{
		post_message("vous", text);
	}

	fetch('/ask',
	{
		method: "POST",
		body: new FormData(document.getElementById("userInput"))
	}).then(response => 
	{
		if (response.ok)
		{
			response.json()
            .then(data => 
            {
            	let place = new Place(data["placeName"], data["informations"], data["longitude"], data["latitude"])

            	post_answer(place);
            })
            .catch(error =>
            {
                console.error(error);
            });
    	}
    	else 
    	{
    		console.error('server response: ' + response.status);
    	}
    }).catch(error =>
    {
    	console.error(error);
	});
}


function post_answer(place)
{
	grandPy = new GrandPy()

	const chatZone = document.getElementById('conversation_screen');


	const bubbleText = document.createElement('li');

	bubbleText.classList.add("bubble_text");
	bubbleText.classList.add("start_allign");


	const header = document.createElement('p');

	header.classList.add("messageHeader");
	header.textContent = "grandPy: ";


	const content = document.createElement('p');


	const introduction = document.createElement('p');
	
	introduction.classList.add('message');
	introduction.textContent = grandPy.succesResponses[aleatory(grandPy.succesResponses.length)];


	const informationsPresentation = document.createElement('p');
	
	informationsPresentation.classList.add('messageHeader');
	informationsPresentation.textContent = grandPy.informations[aleatory(grandPy.informations.length)];


	const informations = document.createElement('p');

	informations.classList.add('message');
	informations.textContent = place["informations"];

	informationsPresentation.appendChild(informations);


	const mapPresentation = document.createElement('p');

	mapPresentation.classList.add('messageHeader');
	mapPresentation.textContent = grandPy.mapIntroductions[aleatory(grandPy.mapIntroductions.length)];


	let mapSection = document.createElement("p");

	mapSection.classList.add('map');

	mapPresentation.appendChild(mapSection);

	content.appendChild(introduction);
	content.appendChild(informationsPresentation);
	content.appendChild(mapPresentation);

	bubbleText.appendChild(header);
	bubbleText.appendChild(content);

	chatZone.appendChild(bubbleText);

	initMap(place);

	chatZone.scrollTop = chatZone.scrollHeight;

}