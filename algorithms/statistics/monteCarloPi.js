var simulations = Math.pow(10, 7);
var circlePoints = 0;
for (var i = 0; i < simulations; i++) {
    var x = Math.random();
    var y = Math.random();
    if (x * x + y * y < 1) {
        circlePoints++;
    }
}
var pi = 4 * circlePoints / simulations;
console.log(pi);
