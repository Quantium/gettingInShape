//Originaly copied from the file ./fibonacci.js. Read it first
//From the original fibonacci excersice I made this other one to demostrate Memoization

//I moved the function to a class, but it's possible to use just a variable for the memoization
class LeonardoBonacci {
    //Let's remember past results
    mem = {0:0, 1:1, 2:1}
    //This function will return the nth number in the fibonacci sequence
    fibonacci(n){
        /////////For benchmarking
        iterations++
        /////////////////////////
    
        //The following lines are for control purposes only
        if(isNaN(n)) return -1
        //We don't need this control because it's is already in the mem variable
        //if(n <= 0) return 0
        //if (n <= 2) return 1

        //This is the magic of memoization, if the result exist there's no need to calculate anything
        if(this.mem[n]) return this.mem[n]

        //We store the result in a variable
        const res = this.fibonacci(n-1) + this.fibonacci(n-2)

        //If the solution hasn't being calculated, then remember it and return the result
        this.mem[n] = res
        return res
    }

    //Removing all the benchmarking an control lines. We could have a single line funciton for fibonacci
    /*
    fib(n){ fib(n-1) + fib(n-2)}
    */
}


// Getting the first console parameter after this file name
const _n = process.argv[2]

/////////For benchmarking
const t0 = Date.now()
let iterations = 0;
/////////////////////////

const lb = new LeonardoBonacci();

let res = []
for (let i = 1; i < _n; i++) {
    res.push(lb.fibonacci(i))
    /*
    res.push(lb.fib(i))
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