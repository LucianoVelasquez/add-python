class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.__edad = edad
    
    @property #Sirve para indicarle que es un getter y poder utilizarla como propiedad.
    def nombre(self):  #Con get podemos acceder a los metodos muy privados.
        return self.__nombre
    @nombre.setter #Con este decorador nos permite modificar las propiedades muy privadas
    def nombre(self,new_nombre):  #Con set podemos modificar a los metodos muy privados.
        self.__nombre = new_nombre
    @nombre.deleter #Sirve para eliminar el valor de la propiedad
    def nombre(self):  
        print('Se elimino correctamentes')
        del self.__nombre
        
ojb = Persona("Mauro",25)
print(ojb.nombre)    
ojb.nombre = "mariano"    
print(ojb.nombre)  

del ojb.nombre
