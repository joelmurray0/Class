//console.log("yo");
//alert("Hello, world!");
//console.log(5 === "5");
//let x = 1;
//let ar = [1, 2, 3];
//const X = 1;

//console.log(ar[1]);

// for (let i = 0; i < 5; i++) {
//   console.log(i);
// }

function greet(name) {
     return `Hello, ${name}!`;
   }
   
   console.log(greet("Alice"));
   
   const counter = document.getElementById("counter");
   const button = document.getElementById("button");
   let n = 0;
   button.addEventListener("click", () => {
     n++;
     counter.innerText = `Counter: ${n}`;
   });
   