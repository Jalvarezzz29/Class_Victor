#Conceptos: conjuntos, intersección, while, random.

import random 

# 1. numeritos aleatorios sin repetir Genera 10 numeritos aleatorios entre 1 y 50 utilizando Guárdalos en un conjunto para evitar duplicados y muestra el conjunto cuando tenga exactamente 10 numeritos diferentes.

def punto1():
    print(" Numeritos aleatorios sin repetir")
    numeros_aleatorios = set()

    while len(numeros_aleatorios) < 10:
        numero = random.randint(1, 50)
        numeros_aleatorios.add(numero)

    print("numeritos aleatorios generados sin repetir :")
    print(numeros_aleatorios)



#2. Lotería de 6 numeritos Simula una lotería generando 6 numeritos únicos entre 1 y 45. Deben almacenarse en un conjunto y mostrarse ordenados de menor a mayor.
def punto2():
    print(" Lotería de 6 numeritos")
    numeros_loteria = set()

    while len(numeros_loteria) < 6:
        numero = random.randint(1, 45)
        numeros_loteria.add(numero)

    print("numeritos de la lotería ordenados: ")
    print(sorted(numeros_loteria))


#3. Adivina el numerito El programa genera un numerito aleatorio entre 1 y 20. El usuario debe adivinarlo. Guarda cada intento en un conjunto para que no se cuenten intentos repetidos.Al finalizar, muestra:  Cantidad de intentos diferentes.  Todos los numeritos que el usuario intentó.
def punto3():
    print(" Adivina el numerito")
    numero_secreto = random.randint(1, 20)
    intentos = set()

    print("Adivina el numerito entre 1 y 20.")

    while True:
        intento = int(input("Introduce tu intento: "))
        intentos.add(intento)

        if intento < 1 or intento > 20:
            print("Por favor, introduce un numerito entre 1 y 20.") 

        elif intento > numero_secreto:
            print("El numerito es menor. Intenta de nuevo.")
        elif intento < numero_secreto:
            print("El numerito es mayor. Intenta de nuevo.")
       
        if intento == numero_secreto:
            print("Felicidades Has adivinado el numero")
            break

    print("Cantidad de intentos diferentes: " + str(len(intentos)))
    print("numeritos que intentaste: " + str(intentos))


#4. Cartas únicas Simula sacar 5 cartas diferentes de una baraja numerada del 1 al 13. Utiliza un conjunto paraimpedir que se repitan cartas.Conceptos: while, random, set.
def punto4():
    print(" Cartas unicas")
    cartas = set()
    while len(cartas) < 5:
        carta = random.randint(1, 13)
        cartas.add(carta)

    print("Cartas sacadas:", cartas)

#5. Dados sin repetir Lanza un dado hasta obtener las 6 caras diferentes (1 al 6). Usa un conjunto para registrar lascaras obtenidas.



def punto5():
    print(" Dados sin repetir")
    caras = set()
    lanzamientos = 0

    while len(caras) < 6:
        cara = random.randint(1, 6)
        caras.add(cara)
        lanzamientos += 1

    print("Numero de lanzamientos:", lanzamientos)
    print("Caras obtenidas:", caras)

#6. Bingo personal Genera automáticamente un cartón con 15 números únicos entre 1 y 75. Después simula el sorteo de números aleatorios hasta que todos los números del cartón hayan salido. Muestra cuántos sorteos fueron necesarios.
 
# ------





#7. Recolectando tesoros En un videojuego aparecen tesoros numerados del 1 al 20. Cada vez que el jugador avanza encuentra un tesoro aleatorio. El programa termina cuando haya encontrado 10 tesoros diferentes. Al final muestra la colección de tesoros.
 
def punto7():
    print(" Recolectando tesoros")
  
    tesoros = set()
    while len(tesoros) < 10:
        tesoro = random.randint(1, 20)
        tesoros.add(tesoro)

    print("Colección de tesoros encontrada:", sorted(tesoros))



#8. Concurso de preguntas Realiza un banco de 20 preguntas numeradas del 1 al 20.Selecciona aleatoriamente 5 preguntas diferentes para un participante sin repetir ninguna.
 

import random

def punto8():
    print(" Concurso de preguntas")
    

    banco_preguntas = {
        1: "¿De qué color es el cielo en un día despejado?",
        2: "¿Cuánto es 2 + 2?",
        3: "¿Cuál es la capital de Francia?",
        4: "¿Cuántos continentes hay en el mundo?",
        5: "¿Cuál es el animal más grande del mundo?",
        6: "¿Cuál es el planeta más cercano al Sol?",
        7: "¿Cuál es el idioma más hablado en el mundo?",
        8: "¿Cuál es la moneda de Estados Unidos?",
        9: "¿Cuál es el océano más grande del mundo?",
        10: "¿Cuál es la montaña más alta del mundo?",
        11: "¿Cuál es el río más largo del mundo?",
        12: "¿Cuál es la capital de España?",
        13: "¿Cuál es el país más grande del mundo?",
        14: "¿Cuál es la capital de Italia?",
        15: "¿Cuál es el continente más poblado del mundo?",
        16: "¿Cuál es la capital de Japón?",
        17: "¿Cuál es el país más pequeño del mundo?",
        18: "¿Cuál es la capital de México?",
        19: "¿Cuál es el planeta más grande del sistema solar?",
        20: "¿Cuál es la capital de Argentina?"
    }

    numeros_seleccionados = set()
    while len(numeros_seleccionados) < 5:
        numero = random.randint(1, 20)
        numeros_seleccionados.add(numero)

    print("Preguntas seleccionadas para el participante:\n")
    for num in sorted(numeros_seleccionados):
        print("Pregunta", num, ":", banco_preguntas[num])



#9. Carrera de colores Existe una lista de colores El programa selecciona aleatoriamente colores hasta obtener 5 colores diferentes. Luego los muestra en el orden en que desees.
 
def punto9():
    print(" Carrera de colores")
  

    colores = ["Rojo", "Azul", "Verde", "Amarillo", "Negro", "Blanco", "Morado", "Naranja"]
    colores_obtenidos = set()

    while len(colores_obtenidos) < 5:
        color = random.choice(colores)
        colores_obtenidos.add(color)

    print("5 colores diferentes obtenidos:", list(colores_obtenidos))


#10. Batalla Pokémon Hay 15 Pokémon disponibles. Cada entrenador debe recibir 6 Pokémon diferentes elegidos aleatoriamente. Al finalizar muestra:  Equipo del Entrenador 1.  Equipo del Entrenador 2.  Los Pokémon que ambos entrenadores tienen en común (si existen).


# ----------





# - - - - - - MENU - - - - - - -


while True: 
    print("- - - - - - - - MENU DE JUEGOS - - - - - - - - -")
    op = int(input("Elija una opción: \n"
    "1. Numeritos aleatorios \n" 
    "2. Lotería \n"
    "3. Adivina el numerito \n"
    "4. Cartas únicas \n"
    "5. Dados sin repetir \n"
    "6. (Proximamnete) Bingo personal \n"
    "7. Recolectando tesoros \n"
    "8. Concurso de preguntas \n"
    "9. Carrera de colores \n"
    "10. (Proximamnete) Batalla Pokémon \n"
    "0. Salir \n"))


    if op == 1:
        punto1()
    elif op == 2:
        punto2()
    elif op == 3:
        punto3()
    elif op == 4:
        punto4()
    elif op == 5:
        punto5()
    elif op == 6:
        print("Proximamente")
    elif op == 7:
        punto7()
    elif op == 8:
        punto8()
    elif op == 9:
        punto9()
    elif op == 10:
        print("Proximamente")
    elif op == 0:
        print("Saliendo del programa...")
        break





