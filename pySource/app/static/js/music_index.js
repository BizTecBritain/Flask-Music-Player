function $(s){
	return document.querySelectorAll(s); 
}

var lis = $("#list li");
var next;

for (var i = 0; i < lis.length; i++){
	lis[i].onclick = function(){
		for (var j = 0; j < lis.length; j++){
			lis[j].className = "";
		}
		this.className = "selected";
		next = "../static/musics/" + this.nextSibling.title
		load("../static/musics/" + this.title)
	}
}

var x = document.createElement("AUDIO");
x.autoplay = true;
x.loop = false;
x.muted = false;
x.onended = function() {
    alert("The audio has ended");
};

function load(url){
	x.src = url;
	x.load();
	playAudio();
}

function playAudio() {
  x.play();
}

function pauseAudio() {
  x.pause();
}

function changeVolume(percent){
	x.volume = percent;
}

$("#volume")[0].onchange = function(){
	changeVolume(this.value/this.max);
	document.getElementById('outvolume').value = this.value;
}
$("#volume")[0].onchange();