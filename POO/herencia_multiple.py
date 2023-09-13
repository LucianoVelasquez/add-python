class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print("hola estoy hablando")


class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        return (f"Mi habilidad es {self.habilidad}")


class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, trabajo, empresa):
        Persona.__init__(self,nombre, edad, nacionalidad) #Constructor Padre
        Artista.__init__(self,habilidad)                  #Constructor Padre
        self.trabajo = trabajo
        self.empresa = empresa

    def presentarse(self):
        print(
            f'Hola mi nombre es {self.nombre} tengo {self.edad} vivo en {self.nacionalidad}, {self.mostrar_habilidad()} y trabajo en {self.empresa}')


new_empleado = EmpleadoArtista('Martin',35,'Argentina','Tenista','Programador','Uala')
new_empleado.presentarse()
new_empleado.hablar()