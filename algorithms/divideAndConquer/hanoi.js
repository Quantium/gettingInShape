let steps = 0
var state = [[],[],[]];

///////////////////////////////////START OF DRAW-FUNCTIONS
const initialize = (s)=>{
    let sequence = [];
    for (let i = 0; i < 7; i++) {
        sequence.push(String.fromCodePoint(128997+i));
    }
    for (let i = 0; i < 2; i++) {
        sequence.push(String.fromCodePoint(11035+i));
    }
    for (let i = 0; i < s; i++) {
        state[0].push(sequence[i%sequence.length])
    }
    state[1]=[];
    state[2]=[];
    console.log("::Initial state::")
    console.log(draw());
    console.log(":::::::::::::::::")
}
const draw = () =>{
    return "A:" + state[0].join("") + " B:" + state[1].join("") + " C:" + state[2].join("");
}
const numberToTower = n =>{
    //65 is the charcode of A
    return String.fromCharCode(64+n);
}
const move = (a,b)=>{
    let from = a-1;
    let to = b-1;
    state[to].push(state[from].pop());;
    console.log("\n", numberToTower(a),"➡️ ", numberToTower(b));
    console.log(draw());
}
///////////////////////////////////END OF DRAW-FUNCTIONS

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
initialize(size);
hanoi(size,1,3)
console.log("Time :: ", Date.now()-t0)
console.log("Steps :: ",steps)
