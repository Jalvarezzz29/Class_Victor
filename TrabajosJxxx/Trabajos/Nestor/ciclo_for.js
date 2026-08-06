// ---------------------------------------
// CICLO FOR - ITERACION DE LISTAS
// ---------------------------------------

// ---- Juan Jose Piedrahita Alvarez ----

// ITERAR = RECORRER 
// ITERAR --> DE FORMA SECUENCIAL 

// ESTRUCTURA:

/* 
for(Inicializacion; Condicion; Incremento){
    // Codigo a ejecutar
}
*/

// EJEMPLOS

// FOR CLASICO --> RECORRER 

console.log("---------------------")

const listaDeLicores = [ "Don julio", "Buchanans", "Aguardiente", "Ron caldas"]

for(let j = 0; j < listaDeLicores.length; j++){
    console.log(listaDeLicores[j]);
}

console.log("---------------------")

const numero = [ 1, 2 , 3, 5, 6]

    console.log(numero.join(",")); 

console.log("---------------------")

// FOR OF --> SIRVE COSAS ITERABLES
// FOR OF --> ARRAY & STRING

const listaDeColores = [ "Rojo", "Azul", "Verde", "Amarillo", "Negro", "Blanco"]

for(color of listaDeColores){ //Color = i
    console.log(color)

}

console.log("---------------------")

// FOR IN --> SIRVE PARA COSAS ENUMERABLES
// FOR IN --> OBJECT

const tiendaDeCelulares = {
 
    // PROPIEDAD (CLAVE): VALOR
 Samsung: 900,
 Apple: 1000,
 Oppo: 300,
 Xiaomi: 600,
 
}

for(let celular in tiendaDeCelulares){
    console.log(celular + ": " + tiendaDeCelulares[celular])

}

