frutas = {"manzana", "cereza", "durazno", "fresa"}

frutas.add("pera")

for Z in frutas:
    print(Z)  

print("banana" in frutas)

# {} CONJUNTOS - DICCIONARIOS & [] ES PARA LISTAS - ESTRUCTURAS DE DATOS
# [] VACIO = L=list() - L=[] & {} VACIO = D=dict() - D={}

print("\n")
print("=======================================================================")
print("\n")

frutas2 = {"mora", "kiwi", "naranja", "sandia"}

frutas2.add("melon")
frutas2.add("mango")
frutas.update(frutas2)

for X in frutas2:
    print(X)
    
print("banana" in frutas2)

