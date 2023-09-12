diccionario = {
    "nombre": "Manuel",
    "apeliddo": "juancarlos",
    "edad": 18
}
# Iterando por clave
for key in diccionario:
    print(key)
# Iterando para obtener key y value. diccionario.items() devuelve una tupla
for datos in diccionario.items():
    key, value = datos
    print(f"La key es: {key} || El value es: {value}")
