//Originaly copied from the file ./fibonacciMemoization.js. Read it first
//From the original Memoization excersice adding a closure function implementation
//We can see that the closure implementation is faster than the class implementation

console.log()
console.log("Memoization Fibonacci Closure")
// Getting the first console parameter after this file name
const _n = process.argv[2]

function memoizeFunction(fn) {
    const cache = {}
    return function(...args) {
        if(cache[args]) return cache[args]
        const res = fn.apply(this, args)
        cache[args] = res
        iterations++;
        return res
    }
}

var fibonacci = memoizeFunction(function(n) {
    return (n === 0 || n === 1) ? n : fibonacci(n - 1) + fibonacci(n - 2);
});

/////////For benchmarking
const t0 = Date.now()
let iterations = 0;
/////////////////////////

let res = []
for (let i = 1; i < _n; i++) {
    res.push(fibonacci(i))
}

/////////For benchmarking
const t1 = Date.now()
const elapsed =  t1-t0;
/////////////////////////

console.log(res)
console.log()
console.log("Elapsed Time :: ", elapsed)
console.log("Iterations :: ", iterations)