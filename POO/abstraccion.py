class Auto:
    def __init__(self):
        self._estado = 'apagado'
    
    def encender(self):
        self._estado = 'encendido'
        print('El auto esta encendido')
    
    def conducir(self): #La abstaccion es ocultar la complegidad interna del sistema
        if self._estado == 'apagado':
            self.encender()
        print('Conduciendo el auto')
        
mi_auto = Auto()
mi_auto.conducir()
