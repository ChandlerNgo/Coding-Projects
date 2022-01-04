const one = document.getElementById("1");
const two = document.getElementById("2");
const three = document.getElementById("3");
const four = document.getElementById("4");
const five = document.getElementById("5");
const six = document.getElementById("6");
const seven = document.getElementById("7");
const eight = document.getElementById("8");
const nine = document.getElementById("9");
const reset = document.getElementById("reset");
const win = document.getElementById("win");

let play = "X";
function next() {
    if (play === "X") {
        play = "O"
    } else {
        play = "X"   
    }
}


one.addEventListener('click', () => {
    document.getElementById("1").innerHTML = play
    next()
})
two.addEventListener('click', () => {
    document.getElementById("2").innerHTML = play
    next()

})
three.addEventListener('click', () => {
    document.getElementById("3").innerHTML = play
    next()

})
four.addEventListener('click', () => {
    document.getElementById("4").innerHTML = play
    next()

})
five.addEventListener('click', () => {
    document.getElementById("5").innerHTML = play
    next()

})
six.addEventListener('click', () => {
    document.getElementById("6").innerHTML = play
    next()

})
seven.addEventListener('click', () => {
    document.getElementById("7").innerHTML = play
    next()

})
eight.addEventListener('click', () => {
    document.getElementById("8").innerHTML = play
    next()

})
nine.addEventListener('click', () => {
    document.getElementById("9").innerHTML = play
    next()

})
reset.addEventListener('click', () =>{
    document.getElementById("1").innerHTML = ""
    document.getElementById("2").innerHTML = ""
    document.getElementById("3").innerHTML = ""
    document.getElementById("4").innerHTML = ""
    document.getElementById("5").innerHTML = ""
    document.getElementById("6").innerHTML = ""
    document.getElementById("7").innerHTML = ""
    document.getElementById("8").innerHTML = ""
    document.getElementById("9").innerHTML = ""
})

