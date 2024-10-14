# Fibonacci

In this folder you will find the function to calculate the [Fibonacci Sequence](https://en.wikipedia.org/wiki/Fibonacci_sequence)

## Recursivity

> "To understand Recursivity you first need to understand Recursivity"

The fibonacci sequence is a good excercise to understand recursivity. Although there are other methods tu solve it, using recursive functions is an elegant, memory saver and funnier way to do it.

A recursive function is a function who calls itself inside its body, a simple example could be:

````` javascript
function sum(arr){
    if(arr.length === 0) return 0
    let val = arr.pop()
    return val + sum(arr)
}
sum([1,2,3,4]) //20
`````

Commonly, the recursive functions always have a logic control statement who stops the execution to avoid stack overflows. In this example is the _if_ of the function which avoids suming 0 forever.

Of course you can perform this sum using loops, but memoization, in most of the cases, saves a lot of memory, sacrificing stack calls wich thanks to modern CPUs is not a big problem anymore

## Memoization

Memoizaton (Yes, without the R) is a programing technique which consist in _save_ or _memorize_ previously calculated values.

Owing to the huge iterations that the implemented fibonacci recursive algorithm can reach, it ir a very good candidate to use memoization

## Testing

To test the fibonacci's implementations execute the next console command:

````shell
N=30; py fibonacci.py $N && node fibonacci.js $N && node fibonacciMemoization.js $N && node fibonacciMemoizationClosure.js $N
````
