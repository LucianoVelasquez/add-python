
#Functions simple
def saludar(nombre):
    print(f"Hola {nombre}")
saludar("Juancito")

#Retornando valores
def retorno(num):
    return num
variable = retorno(5)
print(variable)

#Operador args
def suma(*numeros):
    return numeros
numeros = suma(1,3,4,5,6,7)
print(numeros)