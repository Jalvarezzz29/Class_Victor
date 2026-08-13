// ---------------------------------------
// CICLO WHILE - LOOP
// ---------------------------------------

// ---- Juan Jose Piedrahita Alvarez ----

// ESTRUCTURA:
/*
while(Condicion){
     // CODIGO A EJECUTAR
    // INCREMENTO
}
*/

// EJEMPLO 

let contador = 0;

while(contador < 10){ //WHILE - SE EJECUTA MIENTRAS LA CONDICION ES VERDADERA - SE UTILIZA CUANDO NO SE TIENE EL VALOR A EJECUTAR
    console.log("VALOR  ACTUAL: "+ contador);
    contador++;
}

console.log("---------------------")

// DECREMENTO

let numeroDecrementado = 5;
console.log ("ANTES: " +numeroDecrementado+ " NUMERO DECREMENTADO:", --numeroDecrementado);

let numeroIncrementado = 5;
console.log ("ANTES: " +numeroIncrementado+ " NUMERO INCREMENTADO:", ++numeroIncrementado);

console.log("---------------------")

// LIMITE DE SEGURIDAD - EVITAR BUCLES INFINITOS

let limiteDeSeguridad = 3;

while(limiteDeSeguridad-- > 0){
    console.log("VALOR ACTUAL: ", +limiteDeSeguridad);
}

console.log("---------------------")

let limiteDeSeguridadDos = 100;
let contadorDos = 0;

while(contadorDos < 10 && limiteDeSeguridadDos-- > 0){
    console.log ("LIMITE DE SEGURIDAD EN:" +limiteDeSeguridadDos+ " CONTADOR EN:"+contadorDos);
    contadorDos++;
}

/*
ESTRUCTURA:

do{
   CODIGO A EJECUTAR
   CONTADOR

} While(CONDICION)
*/

console.log("---------------------")

let contadorTres = 0;

do{
    console.log("VALOR ACTUAL:", +contadorTres)
    contadorTres++;
}while(contadorTres < 10)

console.log("---------------------")

// con un do while imprima un mensaje si la edad de el usuario es menor de edad

let edadUsuario = 17;
let limiteDeSeguridadEdad= 1;

while(edadUsuario < 18 && limiteDeSeguridadEdad > 0){
    console.log ("EL USUARIO ES MENOR DE EDAD, TIENE", +edadUsuario+ " AÑOS DE EDAD")
    limiteDeSeguridadEdad--;
}

 console.log("---------------------")

do{
    console.log ("EL USUARIO ES MENOR DE EDAD, TIENE", +edadUsuario+ " AÑOS DE EDAD")
}while(edadUsuario < 18 && limiteDeSeguridadEdad > 0)
