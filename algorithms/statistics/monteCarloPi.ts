//The number of random points to generate. It's set to (10^7) (10 million) to get a more accurate value of π
var simulations:number = Math.pow(10, 7);

//A counter to keep track of the number of points that fall inside the unit circle (x^2 + y^2 < 1)
var circlePoints:number = 0;

for (var i:number = 0; i < simulations; i++) {
    //(x,y) represent the coordinates of a point in a unit square.
    var x:number = Math.random();
    var y:number = Math.random();

    //checks if the point (x, y) lies inside the quarter circle (in the first quadrant) are counted circle by verifying if (x^2 + y^2 < 1).
    if (x * x + y * y < 1) {
        //If true, the point is inside the circle, and the counter is incremented.
        circlePoints++;
    }
}

//This formula estimates \pi because it compares the number of random points inside a quarter unit circle to the total number of points.
//The ratio \frac{\text{circlePoints}}{\text{simulations}} approximates \frac{\pi}{4}, and multiplying by 4 yields an approximation of \pi.
var π:number = 4 * circlePoints / simulations;
console.log(π);

