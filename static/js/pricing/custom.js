
				
				
				
function reply_click()
	{
			var y=event.srcElement.title;
			if (y!=""){
			document.getElementById("ptest").innerHTML+=", "+y
			}
	}

function usunusluge1()
	{
		var str=document.getElementById("ptest").innerHTML;
		if(str!="<b>Wybrane usługi:</b>")
		{
			var fname = str.substring(0, str.lastIndexOf(","));
			document.getElementById("ptest").innerHTML=fname;
		}
	}	
	
function usunusluge2()
	{
		var str=document.getElementById("ptest2").innerHTML;
		if(str!="<b>Cena wybranych usług:</b>")
		{
			var fname = str.substring(0, str.lastIndexOf(","));
			document.getElementById("ptest2").innerHTML=fname;
		}
	}		
	
function usunusluge()
	{
	usunusluge1();
	usunusluge2();
	}	
function myFunction1() 
{
	var x = document.getElementById("id1").value;
	if (x == "1") 
	{
		document.getElementById("zdjcar").style.display = "none";
		document.getElementById("zdjmotor").style.display = "none";
	}else{
		document.getElementById("zdjcar").style.display = "none";
		document.getElementById("zdjmotor").style.display = "none";
	}
	//koło
	if (x == "2") 
	{
		document.getElementById("zdjwheel").style.display = "block";
		document.getElementById("kolo1").style.display="block";
		document.getElementById("kolo2").style.display="block";
		document.getElementById("kolo3").style.display="block";
	}else{
		document.getElementById("zdjwheel").style.display = "none";
		document.getElementById("kolo1").style.display="none";
		document.getElementById("kolo2").style.display="none";
		document.getElementById("kolo3").style.display="none";
	}
	//silnik
	if (x == "3") {
		document.getElementById("zdjengine").style.display = "block";
		document.getElementById("silnik1").style.display="block";
		document.getElementById("silnik2").style.display="block";
		document.getElementById("silnik3").style.display="block";
	}else{
		document.getElementById("zdjengine").style.display = "none";
		document.getElementById("silnik1").style.display="none";
		document.getElementById("silnik2").style.display="none";
		document.getElementById("silnik3").style.display="none";
	}
	//przód
	if (x == "4") {
		document.getElementById("zdjfront").style.display = "block";
		document.getElementById("maska").style.display="block";
		document.getElementById("swiatlop1").style.display="block";
		document.getElementById("swiatlop2").style.display="block";
		document.getElementById("kierunkowskaz1").style.display="block";
		document.getElementById("kierunkowskaz2").style.display="block";
	}else{
		document.getElementById("zdjfront").style.display = "none";
		document.getElementById("maska").style.display="none";
		document.getElementById("swiatlop1").style.display="none";
		document.getElementById("swiatlop2").style.display="none";
		document.getElementById("kierunkowskaz1").style.display="none";
		document.getElementById("kierunkowskaz2").style.display="none";
	}
	//tył
	if (x == "5") {
		document.getElementById("zdjback").style.display = "block";
		document.getElementById("swiatlot1").style.display="block";
		document.getElementById("swiatlot2").style.display="block";
		document.getElementById("kierunkowskaz3").style.display="block";
		document.getElementById("kierunkowskaz4").style.display="block";
	}else{
		document.getElementById("zdjback").style.display = "none";
		document.getElementById("swiatlot1").style.display="none";
		document.getElementById("swiatlot2").style.display="none";
		document.getElementById("kierunkowskaz3").style.display="none";
		document.getElementById("kierunkowskaz4").style.display="none";
	}
	//kokpit
	if (x == "6") {
		document.getElementById("zdjinside").style.display = "block";
		document.getElementById("szybap").style.display="block";
		document.getElementById("kierownica").style.display="block";
		document.getElementById("drzwi").style.display="block";
		document.getElementById("drzwi2").style.display="block";
		document.getElementById("lusterko1").style.display="block";
		document.getElementById("lusterko2").style.display="block";
		document.getElementById("hamulec").style.display="block";
		document.getElementById("radio").style.display="block";
		
	}else{
		document.getElementById("zdjinside").style.display = "none";
		document.getElementById("szybap").style.display="none";
		document.getElementById("kierownica").style.display="none";
		document.getElementById("drzwi").style.display="none";
		document.getElementById("drzwi2").style.display="none";
		document.getElementById("lusterko1").style.display="none";
		document.getElementById("lusterko2").style.display="none";
		document.getElementById("hamulec").style.display="none";
		document.getElementById("radio").style.display="none";
	}
		
			
}

