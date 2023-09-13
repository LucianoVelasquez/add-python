#Se encarga de proteger propiedades de las clases.
class MiClase:
    def __init__(self):
        self._atributo_privado = 'algo' #Con piso indicamos que es un atributo privado
        self.__atributo_muy_privado = 'algo' #Para acceder a ellos se usan los Seters y Getters.
    
    def __hablar(self):
        print('Hola soy un metodo muy privado')
        
obj = MiClase();
print(obj.__atributo_muy_privado)
obj.__hablar()