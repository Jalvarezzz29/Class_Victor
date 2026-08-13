class artista:
    def __init__(self, talento):
        self.talento = talento
    
    def mostrar_talento(self):
        return f"Mi talento es {self.talento}."
    
class empleadoArtista(artista):
    def __init__(self, talento, nombre, edad, altura, salario, empresa):
        super().__init__(talento)
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.salario = salario
        self.empresa = empresa
        
        super().__init__(nombre,edad, altura)
        artista.__init__(talento)
        self.salario = salario
        self.empresa = empresa

    def hablar(self):
        return f"Hola, soy {self.nombre}, {self.mostrar_talento()}, tengo {self.edad} años, mido {self.altura} cm, gano {self.salario} y trabajo en {self.empresa}."