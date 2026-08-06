/* JUAN JOSE PIEDRAHITA ALVAREZ - ANALISIS Y DESARROLLO DE SOFTWARE 
PIEDRAHITAJUANJOSE31@GMAIL.COM - 3007746906 - FICHA 3408936 */

// 1. Contador del 1 al 10

let i = 1;
while (i <= 10) {
    console.log(i);
    i++;
}

console.log("---------------------------------");

// 2. Contador descendente del 10 al 1 

let j = 10;
do {
    console.log(j);
    j--;
} while (j >= 1);

console.log("---------------------------------");

// 3. Suma de los primeros 100 números naturales

let suma = 0;
let contador = 1;
while (contador <= 100) {
    suma += contador;
    contador++;
}
console.log("Suma de 1 a 100:", +suma);

console.log("---------------------------------");

// 4. Validar entrada del usuario (NO)

// 5. Suma de pares entre 1 y 50 (while)
let sumaPares = 0;
let num = 1;
while (num <= 50) {
    if (num % 2 === 0) {
        sumaPares += num;
    }
    num++;
}
console.log("Suma de pares:", sumaPares);

console.log("---------------------------------");

// 6. Bucle con seguridad
let limite = 0;
while (true) {
    limite++;
    console.log("Repetición:", limite);
    if (limite === 5) {
        break;
    }
}

console.log("---------------------------------");

// 7. Comparar comportamiento
let x = 20;
while (x < 10) {
    console.log("While: No se ejecuta porque 20 < 10 es falso desde el inicio.");
}
do {
    console.log("Do While: Se ejecuta esta única vez porque primero actúa y luego evalúa la condición.");
} while (x < 10);