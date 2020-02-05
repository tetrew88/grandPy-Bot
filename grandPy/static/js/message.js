function post_message(senderName, message)
{
	const chatZone = document.getElementById('conversation_screen');

	const newElement = document.createElement('li');

	newElement.classList.add("bubble_text");
	newElement.textContent = senderName + ": " + message;

	if(senderName == "grandPy")
	{
		newElement.classList.add("start_allign");	
	}
	else
	{
		newElement.classList.add("end_allign");
		newElement.style.backgroundColor = "green";
	}

	chatZone.appendChild(newElement);

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
	}).then(response => {
		if (response.ok)
		{
			response.text()
            .then(console.log)
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