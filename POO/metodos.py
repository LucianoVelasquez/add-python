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
         
celular_1 = Celular('Samsung',"S75","45mpx")
celular_1.llamar()      
celular_1.cortar()