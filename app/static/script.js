
function clickButton(){
	window.open("static/lineup.html","_self");
}

/***********DECLARATION******************/
var main2= document.querySelector(".main2");
/******4-3-3*****/
var formation=document.getElementById("formation");
var opt1=document.getElementById("opt1");
var formation0=document.querySelector(".formation0")
var formation1= document.querySelector(".formation1");
var block= document.querySelectorAll(".block");
var players=document.querySelectorAll(".p");
var forward=document.querySelectorAll(".w");
var mid=document.querySelectorAll(".x");
var defense=document.querySelectorAll(".y");
var goalkeeper=document.querySelectorAll(".z");
/******4-4-2*****/
var formation2=document.querySelector(".formation2");
var block2= document.querySelectorAll(".block2");
var players2=document.querySelectorAll(".p2");
var forward2=document.querySelectorAll(".w2");
var mid2=document.querySelectorAll(".x2");
var defense2=document.querySelectorAll(".y2");
var goalkeeper2=document.querySelectorAll(".z2");

var first=document.getElementById("first");
var second=document.getElementById("second");
var third=document.getElementById("third");

/*********FUNCTIONS*********************/

formation.addEventListener("change",Tactic433);


function Tactic433(){
	if(formation.options[1].selected == true){

		formation0.classList.remove("formation0");
		formation2.classList.remove("field2");
		formation1.classList.add("field");
		for(var i=0; i<4; i++){
			block[i].classList.add("lines");
		}
		block[0].classList.add("line1")
		block[1].classList.add("line2");
		block[2].classList.add("line3");
		block[3].classList.add("line4");

		for(var i=0; i<11; i++){
			players[i].classList.add("placePlayer");
		}

		for(var i=0; i<forward.length; i++){
			forward[i].classList.add("forward");
		}
		for(var i=0; i<mid.length; i++){
			mid[i].classList.add("mid");
		}
		for(var i=0; i<defense.length; i++){
			defense[i].classList.add("defense");
		}
		for(var i=0; i<goalkeeper.length; i++){
			goalkeeper[i].classList.add("goalkeeper");
		}
	}

	else if(formation.options[2].selected == true){
		
		// deletefirst();
		deletesecond();
		// addthird();

		formation0.classList.remove("formation0");
		formation1.classList.remove("field");
		formation2.classList.add("field2");

		for(var i=0; i<4; i++){
			block2[i].classList.add("linesbis");
		}
		block2[0].classList.add("line1bis")
		block2[1].classList.add("line2bis");
		block2[2].classList.add("line3bis");
		block2[3].classList.add("line4bis");

		for(var i=0; i<players2.length; i++){
			players2[i].classList.add("placePlayerbis");
		}

		for(var i=0; i<forward2.length; i++){
			forward2[i].classList.add("forwardbis");
		}
		for(var i=0; i<mid2.length; i++){
			mid2[i].classList.add("midbis");
		}
		for(var i=0; i<defense2.length; i++){
			defense2[i].classList.add("defensebis");
		}
		for(var i=0; i<goalkeeper2.length; i++){
			goalkeeper2[i].classList.add("goalkeeperbis");
		}
	}
	else{
		deletethird();
		formation0.classList.add("formation0");
		formation1.classList.remove("field");
		formation2.classList.remove("field2");
	}	
}

function deletformation(){


	// for(var i=0; i<4; i++){
	// 	block[i].classList.remove("lines");
	// }
	// block[0].classList.remove("line1")
	// block[1].classList.remove("line2");
	// block[2].classList.remove("line3");
	// block[3].classList.remove("line4");
	// for(var i=0; i<11; i++){
	// 	players[i].classList.remove("placePlayer");
	// }

	// for(var i=0; i<forward.length; i++){
	// 	forward[i].classList.remove("forward");
	// }
	// for(var i=0; i<mid.length; i++){
	// 	mid[i].classList.remove("mid");
	// }
	// for(var i=0; i<defense.length; i++){
	// 	defense[i].classList.remove("defense");
	// }
	// for(var i=0; i<goalkeeper.length; i++){
	// 	goalkeeper[i].classList.remove("goalkeeper");
	// }
}

function deletefirst(){
	first.parentNode.removeChild(first);

}
function deletesecond(){
	second.parentNode.removeChild(second);
}
function deletethird(){
	third.parentNode.removeChild(third);
}

function addfirst(){
	document.createElement(first);
	main2.appendChild(first);
}

function addsecond(){
	document.createElement(second);
	// main2.appendChild(second);
}

function addthird(){
	document.createElement(third);
	main2.appendChild(third);
}