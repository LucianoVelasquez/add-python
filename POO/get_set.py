class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.__edad = edad
    
    def get_nombre(self):  #Con get podemos acceder a los metodos muy privados.
        return self.__nombre
    def set_nombre(self,new_nombre):  #Con set podemos modificar a los metodos muy privados.
        self.__nombre = new_nombre

ojb = Persona('mi nombre',23)
print(ojb.get_nombre())       
ojb.set_nombre('nuevo nombre')
print(ojb.get_nombre())
        
        