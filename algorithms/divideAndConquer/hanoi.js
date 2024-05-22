let steps = 0

// TODO: Implementar movimiento real 
const move = (a,b)=>{
    //console.log(a,"➡️",b)
}
const hanoi = (n,from,to)=>{
    steps++
    if(n===1){
        return move(from,to)
    }
    const third = 6 - (from+to)

    // Recursivo
    hanoi(n-1,from,third)
    move(from,to)
    hanoi(n-1,third,to)
}

const size = 0 | process.argv[2]

const t0 = Date.now()
hanoi(size,1,3)
console.log("Time :: ", Date.now()-t0)
console.log("Steps :: ",steps)