class Camisa():
    def __init__(self,marca, talla, color, precio):
        self.marca = marca
        self.talla = talla
        self.color = color
        self.precio = precio
    
    def Lavar(self):
        print("ESTIVEN ESTA LAVANDO UNA CAMISA", self.marca, "DE TALLA",self.talla, "COLOR", self.color, "Y PRECIO", self.precio)
        
        print("------------------------------------")
    def Planchar(self):
        print("JUAN ESTA PLANCHADO UNA CAMISA", self.marca, "DE TALLA",self.talla, "COLOR", self.color, "Y PRECIO", self.precio)
    
        print("------------------------------------")
    
Camisa_estiven = Camisa("Nike", "M", "Gris", "500K")

Camisa_estiven.Lavar()

Camisa_juan = Camisa("Puma", "M", "Negro", "300K")

Camisa_juan.Planchar()

Camisa_samuel = Camisa("Adidas", "M", "Blanco", "250K")

        
print("LA CAMISA DE ESTIVEN ES DE LA MARCA", Camisa_estiven.marca,"TALLA", Camisa_estiven.talla,"COLOR", Camisa_estiven.color,"Y TIENE UN PRECIO DE", Camisa_estiven.precio)
print("------------------------------------")
  
print("LA CAMISA DE JUAN ES DE LA MARCA", Camisa_juan.marca,"TALLA", Camisa_juan.talla,"COLOR", Camisa_juan.color,"Y TIENE UN PRECIO DE", Camisa_juan.precio)
print("------------------------------------")

print("LA CAMISA DE SAMUEL ES DE LA MARCA", Camisa_samuel.marca,"TALLA", Camisa_samuel.talla,"COLOR", Camisa_samuel.color,"Y TIENE UN PRECIO DE", Camisa_samuel.precio)
print("------------------------------------")

class moto():
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        
    def Limpiar(self):
            print("EL USUARIO ESTA LIMPIANDO UNA MOTO", self.marca, "MODELO",self.modelo, "COLOR", self.color)
        
input_marca = input("Digite la marca de la moto:")
input_modelo = input("Digite el modelo de la moto:")
input_color = input("Digite el color de la moto:")

moto_usuario = moto(input_marca, input_modelo, input_color)
moto_usuario.Limpiar()
