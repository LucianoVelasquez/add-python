diccionario = {
    "nombre" : 'luciano',
    "apellido" : 'velasquez',
    "subs": 800
}
#Muestra todas las keys
keys = diccionario.keys()
print(keys)

#Get muetra el valor de una key
value = diccionario.get("nombre")
print(value)

#Pop Eliminando un elemento de dic
diccionario.pop('nombre')
print(diccionario)

#Clear, elimina el diccionario
print(diccionario.clear())