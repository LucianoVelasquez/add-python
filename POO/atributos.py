#Atributos
#Propiedades de instancia
class Autos:
    def __init__(self,marca,modelo,puertas):  #Funcion constructura
        self.marca = marca
        self.modelo = modelo
        self.puertas = puertas

new_auto = Autos("BMW","S56",4)
print(f"Marca:{new_auto.marca} || Modelo:{new_auto.modelo} || Puertas:{new_auto.puertas}")  