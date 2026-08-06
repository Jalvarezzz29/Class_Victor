# JUAN JOSE PIEDRAHITA ALVAREZ - 3408960 - ADSO 

# 1. Solicite un numero entero al usuario y determine si es positivo, negativo o igual a cero. Muestre elresultado correspondiente.

input_numero = int(input("Digite un numero entero: "))

if input_numero > 0:
    print("El numero es positivo.")
elif input_numero < 0:
    print("El numero es negativo.")
else:
    print("El numero es igual a cero.")
    
    
# 2. Solicite el valor de una compra y aplique el descuento según el monto establecido. Al finalizar, muestre el descuento aplicado y el total a pagar.

input_compra = float(input("Digite el valor de la compra: "))

if input_compra >= 100:
    descuento = input_compra * 0.15
    total_pagar = input_compra - descuento
    print(f"El descuento aplicado es: {descuento}")
    print(f"El total a pagar es: {total_pagar}")
else:
    print(f"No se aplica descuento.")
    print(f"El total a pagar es:{input_compra}")
    
# 3. Con ciclo While : Permita ingresar numeros de forma repetitiva hasta que el usuario decida finalizar. Al terminar,muestre la cantidad de numeros ingresados y la suma total.

cantidad_numeros = 0
suma_total = 0

while True:
    numero = float(input("Digite un numero (Si digita 0 es para finalizar): "))
    if numero == 0:
        break
    cantidad_numeros += 1
    suma_total += numero

print(f"La cantidad de numeros ingresados es: {cantidad_numeros}")
print(f"La suma total es: {suma_total}")

# 4. Con ciclo While: Genere un numero aleatorio entre 1 y 20 y permita que el usuario intente adivinarlo. El programa debe indicar la cantidad de intentos realizados hasta acertar.

import random

numero_aleatorio = random.randint(1, 20)
intentos = 0

while True:
    intento = int(input("Adivina el numero (entre 1 y 20): "))
    intentos += 1
    if intento == numero_aleatorio:
        print(f"Acertaste El numero era {numero_aleatorio}")
        print(f"La cantidad de intentos realizados fueron: {intentos}")
        break
    
    elif intento < numero_aleatorio:
        print("El numero es mayor.")
    else:
        print("El numero es menor.")
        
# 5. Con ciclo For: Solicite un numero entero y muestre su tabla de multiplicar del 1 al 10 utilizando un ciclo for.

numero = int(input("Digite un numero entero para ver su tabla de multiplicacion: "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

# 6. Con ciclo For: Solicite la cantidad de estudiantes y registre la nota de cada uno. Al finalizar, muestre el promedio del grupo, la nota más alta, la más baja y la cantidad de estudiantes aprobados y reprobados.

cantidad_estudiantes = int(input("Digite la cantidad de estudiantes: "))

for i in range(cantidad_estudiantes):
    
    nota = float(input(f"Digite la nota del estudiante {i + 1}: "))
    if i == 0:
        suma_notas = nota
        
        nota_alta = nota
        
        nota_baja = nota
        
        cantidad_aprobados = 0
        
        cantidad_reprobados = 0
    else:
        suma_notas += nota
        
        if nota > nota_alta:
            nota_alta = nota
            
        if nota < nota_baja:
            nota_baja = nota

    if nota >= 3.0:
        cantidad_aprobados += 1
    else:
        cantidad_reprobados += 1

promedio = suma_notas / cantidad_estudiantes

print(f"El promedio del grupo es: {promedio}")
print(f"La nota más alta es: {nota_alta}")
print(f"La nota más baja es: {nota_baja}")
print(f"La cantidad de estudiantes aprobados es: {cantidad_aprobados}")
print(f"La cantidad de estudiantes reprobados es: {cantidad_reprobados}")
