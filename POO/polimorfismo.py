#Hace referencia a que se le puede enviar un mismo mensaje a diferentes objetos y estos son capases de dar diferentes respuestas (Por sus propiedades).
#En los lenguajes de tipados dinamicos no es necesario hacer un polimorfismo de herencia

class Gato():
    def sonido(self):
        return 'Miau'
class Perro():
    def sonido(self):
        return 'Guau'

gato = Gato()
perro = Perro()

print(gato.sonido())
print(perro.sonido())        