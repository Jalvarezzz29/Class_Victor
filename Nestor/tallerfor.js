/* JUAN JOSE PIEDRAHITA ALVAREZ - ANALISIS Y DESARROLLO DE SOFTWARE 
PIEDRAHITAJUANJOSE31@GMAIL.COM - 3007746906 - FICHA 3408936 */

// 1. FOR CLÁSICO
let nombres = ["Ana", "Pedro", "María", "Juan", "Sofía"];
for (let i = 0; i < nombres.length; i++) {
     console.log("Nombre: " + nombres[i] + " - Letras: " + nombres[i].length);
}

console.log("---------------------------------");

// 2. FOR OF CON STRINGS
let frase = "Hola";
for (let letra of frase) { 
    console.log(letra); 
}

console.log("---------------------------------");

// 3. FOR OF CON ARRAYS
let frutas = ["Manzana", "Plátano", "Fresa"];
for (let fruta of frutas) { 
    console.log("Me gusta la fruta: " + fruta); 
}

console.log("---------------------------------");

// 4. FOR IN CON OBJETOS
let producto = { nombre: "Camiseta", precio: 15.99, categoria: "Ropa" };
for (let clave in producto) { 
    console.log(clave + ": " + producto[clave]); 
}

console.log("---------------------------------");

// 5. COMPARACIÓN
let numeros = [10, 20, 30];
for (let i = 0; i < numeros.length; i++) { 
    console.log("Clásico: " + numeros[i]); 
}
for (let num of numeros) { 
    console.log("For of: " + num); 
}

/* ME PARECCIO MUCHO MAS FACIL UTILIZAR UN FOR OF POR LA SIMPLE Y SENCILLA RAZON QUE NECESITA 
SIMPLEMENTE UNA CLAVE PARA LLAMAR LOS VALORES DE UN ARRAY, MIENTRAS QUE EL FOR CLÁSICO NECESITA 
UNA VARIABLE PARA CONTAR LOS CICLOS Y UNA CLAVE PARA LLAMAR LOS VALORES, LO QUE HACE QUE SEA MÁS 
LARGO Y NO SE PRIORICE EL AHORRO DE LINEAS.*/