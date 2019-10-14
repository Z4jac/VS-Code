//funkcja random
var random = Math.floor(Math.random());

function randomeWhole(ourMin = 1, ourMax = 6) {
	return Math.floor(Math.random() * (ourMax - ourMin + 1)) + ourMin;
}


//oblicza średnią wypadania liczb
/*
var one = 0;
var two = 0;
var three = 0;
var four = 0;
var five = 0;
var six = 0;
function avrg() {
	for (var i = 0; i <= 10000; i++) {
		var d = randomeWhole(1, 6);
		switch (d) {
			case 1:
				one += 1;
				break;
			case 2:
				two += 1;
				break;
			case 3:
				three += 1;
				break;
			case 4:
				four += 1;
				break;
			case 5:
				five += 1;
				break;
			case 6:
				six += 1;
				break;
		}
	}
}
avrg();
console.log(one, two, three, four, five, six);
*/
