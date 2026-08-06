
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hablar(self):
        return "Hace un sonido"

class Perro(Animal):
    def hablar(self):
        return f"{self.nombre} dice: Guau"

class Gato(Animal):
    def hablar(self):
        return f"{self.nombre} dice: Miau"


mi_perro = Perro("Max")
mi_gato = Gato("Sam")

print(mi_perro.hablar())  
print(mi_gato.hablar())   