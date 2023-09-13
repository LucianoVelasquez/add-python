from abc import ABC, abstractclassmethod 
#Plantilla que nos permite crear Personas, es una plantilla unica. Esta plantilla obliga a todas las clases que la implementen a que usen sus metodos y propiedades (asegura el polimorfismo).

class Persona(ABC):
    @abstractclassmethod
    def __init__(self,nombre,edad,sexo,actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
        
    @abstractclassmethod
    def hacer_actividar(self):
        pass    
    
    def presentarse(self):
        print(f'Hola me llamo {self.nombre} y tengo {self.edad}')
        
        
class Estudiante(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)
    def hacer_actividar(self):
        print(f'Estoy estudiando {self.actividad}')  
                  
class Trabajador(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)
    def hacer_actividar(self):
        print(f'Estoy trabajando en el rubro de {self.actividad}')            
        
objeto_1 = Estudiante('mariano',23,'hombre','programacion')
objeto_2= Trabajador('Pedrito',55,'Hombre','Cajero')
objeto_1.presentarse()
objeto_1.hacer_actividar()    
objeto_2.presentarse()
objeto_2.hacer_actividar()