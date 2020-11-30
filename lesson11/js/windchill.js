var t = document.getElementById("high").innerHTML;
var s = document.getElementById("speed").innerHTML;
t = parseInt(t)
s = parseInt(s)
if(t<=50 && s >= 3.0){
    var wc 
    wc = 35.74 + (0.6215 * t) - (35.75* s**0.16)+ (0.4275 * t * (s **0.16))
    wc = Math.round(wc)
}
else{
    wc = "N/A"
}

document.getElementById("chill").innerHTML = wc
