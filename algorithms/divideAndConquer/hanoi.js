let steps = 0

// TODO: Implementar movimiento real 
const move = (a,b)=>{
    //console.log(a,"➡️",b)
}
const hanoi = (n,start,target)=>{
    steps++
    if(n===1){
        return move(start,target)
    }

    // La suma de los números que representan a las 3 clavijas siempre es 1 + 2 + 3 = 6, 
    // si conocemos 2 de las claviijas (start y target), podemos encontrar la tercera usando la fórmula:
    // \text{third} = 6 - (\text{start} + \text{target})
    const other = 6 - (start+target)

    // Recursivo
    hanoi(n-1,start,other) // Hey, guy(s) above me, move from top of me (start) to the peg (other) that is not my target
    move(start,target) // I will move to my target
    hanoi(n-1,other,target) // Finally, you move from the peg you are in (other) back on top of me (target)

}

const size = 0 | process.argv[2]

const t0 = Date.now()
hanoi(size,1,3)
console.log("Time :: ", Date.now()-t0)
console.log("Steps :: ",steps)