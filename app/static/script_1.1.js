//******* lineup page access button **** ////
function clickButton(){
	window.open("lineup.html","_self");
}

/***********DECLARATION******************/
var main2= document.querySelector(".main2");
/******4-3-3*****/
var formation_choice=document.getElementById("formation_selection");
//var opt1=document.getElementById("opt1");
var formation0=document.querySelector(".formation0")  // init empty field block 
var formation1= document.querySelector(".formation_433"); // field block 4-3-3
var block= document.querySelectorAll(".block");
var players=document.querySelectorAll(".p"); // .p 
var forward=document.querySelectorAll(".w"); // .w
var mid=document.querySelectorAll(".x"); // .x
var defense=document.querySelectorAll(".y"); //.y 
var goalkeeper=document.querySelectorAll(".z"); //.z
/******4-4-2*****/
var formation2=document.querySelector(".formation_442"); // field block 4-4-2
var block2= document.querySelectorAll(".block2");
var players2=document.querySelectorAll(".p2"); // .p2
var forward2=document.querySelectorAll(".w2"); // .w2
var mid2=document.querySelectorAll(".x2"); // .x2
var defense2=document.querySelectorAll(".y2"); // .y2
var goalkeeper2=document.querySelectorAll(".z2"); // .z2
// ***** upper nodes for clean up *****/////
var first=document.getElementById("first");
var second=document.getElementById("second");
var third=document.getElementById("third");



var positionA1=document.getElementById("A1");

var input1=document.getElementById("input1");

// var valueA1=input1.value;

											  

												 

var button= document.getElementById("button");

button.addEventListener("click", function(){
	var valueA1=input1.value;
	positionA1.innerHTML= valueA1;
})


/*********FUNCTIONS*********************/

formation_choice.addEventListener("change",Tactic);



function Tactic(){

	///// *****  Choice is 4-3-3 ****  //////////

	if(formation_choice.options[1].selected == true)

	{

		
		formation0.classList.remove("formation0");

        //formation2.classList.remove("players2");
		//formation2.classList.remove("block2");
		formation2.classList.remove("field2");
		


        if (document.body.contains(third)!==false)
		{
			delete_Field(third,third);
         }



        if (document.body.contains(second)==false)
		{
			main2.insertBefore(second,document.querySelector(".choosePlayers"));
         }


		formation1.classList.add("field");
		
        /// ****** fill lines blocks ****/////
        for(var i=0; i<4; i++){
        	block[i].classList.add("lines");
        	block[i].classList.add(String("line" + i + ""));
        }

        
        ///// palyers //////
        for(var i=0; i<11; i++){
        	players[i].classList.add("placePlayer");
        }


        ///// **** position : strike / mid / def / GK ****/////

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

    ///// *****  Choice is 4-4-2 ****  //////////

    else if(formation_choice.options[2].selected == true){


        if (document.body.contains(third)==false)
		{main2.insertBefore(third,document.querySelector(".choosePlayers"));}
        

        if (document.body.contains(second)!==false)
		{
			delete_Field(second,second);
         }

	    formation0.classList.remove("formation0");
		formation1.classList.remove("field");
		formation2.classList.add("field2");



		for(var i=0; i<4; i++){
			block2[i].classList.add("linesbis");
			block2[i].classList.add(String("line" + i + "bis"));
		}
		

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
	else

	{
		//delete_Field(second,second);

        if (document.body.contains(second)!==false)
		{
			delete_Field(second,second);
         }



        if (document.body.contains(third)!==false)
		{
			delete_Field(third,third);
         }




		formation0.classList.add("formation0");
		formation1.classList.remove("field");
		formation2.classList.remove("field2");

	}	
}


function delete_Field(parent, child)
{
	
	parent.parentNode.removeChild(child);
}



function remove_Class()
{

  

}

function add_Field(parent,child)
{

	//if (parent == undefined || child == undefined)

	//{
     //document.createElement(child);
     parent.appendChild(child);
	//}

}

