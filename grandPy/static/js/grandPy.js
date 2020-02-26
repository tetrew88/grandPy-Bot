class GrandPy
{
	constructor()
	{
		this.salutations = ["Hello World !", "Bienvenue jeune curieu(x)(euse) !"];
		this.presentations = ["Je suis le vieux grandPy.", "Mon surnom est grandPy."];
		this.succesResponses = ["J'ai trouver !", "Bingo !", "Excelsior !"];
		this.errors = ["je suis désoler je n'arrive pas a me souvenir.", "mon vieux cerveaux a du disjoncter je ne trouve pas la réponse."];
		this.informations = ["Voici quelque petite information sur le lieux: ", "Bon a savoir: "];
		this.mapIntroductions = ["Je t'ai déssiner une petite carte: ", "voici une carte pour t'aider a trouver: "];
		this.ask = "";

		this.say_hello = say_hello(this);

		function say_hello(obj)
		{
			let aleatoryNumber = aleatory(obj.salutations.length);
			
			let salutation =  obj.salutations[aleatoryNumber] + " " + obj.presentations[aleatoryNumber]
			
			post_message('grandPy', salutation);
		}


	}	
}


function aleatory(x)
{
	return (Math.floor((x)*Math.random()));
}