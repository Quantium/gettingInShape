//To test this write in your console
//>  node fibonacci.js N
// Where N is the lenght of the array you want to get of the fibonacci sequence
//Example:
//  node fibonacci.js 6
//[ 0, 1, 1, 2, 3, 5 ]

//This function will return the nth number in the fibonacci sequence
const fibonacci = n => {
    /////////For benchmarking
    iterations++
    /////////////////////////

    //The following lines are for control purposes only
    if(isNaN(n)) return -1
    if(n <= 0) return 0
    if (n <= 2) return 1

    return fibonacci(n-1) + fibonacci(n-2);
}

//Removing all the benchmarking an control lines. We could have a single line funciton for fibonacci
/*
const fib = n => fib(n-1) + fib(n-2);
*/

// Getting the first console parameter after this file name
const _n = process.argv[2]

/////////For benchmarking
const t0 = Date.now()
let iterations = 0;
/////////////////////////

let res = []
for (let i = 1; i < _n; i++) {
    res.push(fibonacci(i))
    /*
    res.push(fib(i))
    */
}

/////////For benchmarking
const t1 = Date.now()
const elapsed =  t1-t0;
/////////////////////////

console.log(res)
console.log()
console.log("Elapsed Time :: ", elapsed)
console.log("Iterations :: ", iterations)