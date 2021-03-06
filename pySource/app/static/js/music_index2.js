function $(s){
	return document.querySelectorAll(s); 
}

var lis = $("#list li");

for (var i = 0; i < lis.length; i++){
	lis[i].onclick = function(){
		for (var j = 0; j < lis.length; j++){
			lis[j].className = "";
		}
		this.className = "selected";
		load("../static/musics/" + this.title)
	}
}

var xhr = new XMLHttpRequest();
var ac = new (window.AudioContext||window.webkitAudioContext)();
var gainNode = ac[ac.createGain? "createGain":"createGain"]();
gainNode.connect(ac.destination);


var analyser = ac.createAnalyser();
var size = 128;
analyser.fftSize = size * 2;
analyser.connect(gainNode);


var source = null;

var count = 0;

function load(url){
	var n = ++count;
	source && source[source.stop ? "stop": "noteOff"]();
	xhr.abort();
	xhr.open("GET", url);
	xhr.responseType = "arraybuffer";
	xhr.onload = function(){
		if (n != count) return;
		ac.decodeAudioData(xhr.response, function(buffer){
			if (n != count) return;
			var bufferSource = ac.createBufferSource();
			bufferSource.buffer = buffer;
			bufferSource.connect(analyser);
			bufferSource[bufferSource.start?"start":"noteOn"](0);
			source = bufferSource;
		}, function(err){
			console.log(err);
		});
	}
	xhr.send();
}

function changeVolume(percent){
	gainNode.gain.value = percent * percent;
}

$("#volume")[0].onchange = function(){
	changeVolume(this.value/this.max);
	document.getElementById('outvolume').value = this.value;
}
$("#volume")[0].onchange();