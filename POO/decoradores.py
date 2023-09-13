#Un decorador toma una funcion de entrada, le agrega una funionalidad extra y devuelve una funcion modificada

def decorador(funcion):
    def funcion_modificada():
        print("Antes de llamar a la funcion")
        funcion()
        print("Despues de llamar a la funcion")
    return funcion_modificada 
#Ejemplo de decorador 
"""    
def saludos():
    print("Hola soy un saludos")
saludo_modificado = decorador(saludos)
saludo_modificado()   """  

#Fomra correcta de implementarlo.
@decorador
def saludos():
    print("hola soy un saludo")
saludos()    
