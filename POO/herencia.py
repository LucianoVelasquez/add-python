#Una clase hija puede heredar todos los atributos y metodos de la clase padre.
#Herencia simple.
class Celular:
    def __init__(self,marca,modelo,camara): #Funcion constructura.
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
        
    #Metodos
    def llamar(self):
        print(f'Estas haciendo un llamado con el celular: {self.marca}, {self.modelo}') 
    def cortar(self):
        print(f'Cortaste la llamda con el celular: {self.marca}, {self.modelo}')      
        
class Smartphone(Celular): #Usamos los parentecis y dentro invocamos a la clase celular, para poder usar la herencia.
    def __init__(self, marca, modelo, camara,pantalla,): #Declarando constructor.
        super().__init__(marca, modelo, camara) #Declarando el constructor padre
        
        self.pantalla = pantalla

           
celular_1 = Smartphone('Samsung',"S75","45mpx","4,7")
celular_1.llamar()
print(celular_1.pantalla)