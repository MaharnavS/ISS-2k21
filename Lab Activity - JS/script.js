var i = 0;
var texts = ["Hello","Bonjour","Adios","Hola","Guten Tag","Salve","Asalaam Alaikum","Konnichiwa"];
var index = 0;
var speed = 150;
var count = 0;

function typeWriter() 
{
	if(count < texts[index].length)
		{
			if (i < texts[index].length) 
				{
					document.getElementById("Type-anim").innerHTML += texts[index].charAt(i);
					i++;
					count++;
					setTimeout(typeWriter, speed);
				}
		}
	else 
		{
			document.getElementById("Type-anim").innerHTML = texts[index].substring(0, i);
			i--;
			if (i < 0)
				{
					count = 0;
					i = 0;
					index = (index+1)%(texts.length);
				}
			setTimeout(typeWriter, speed);
		}
}

typeWriter();