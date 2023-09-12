# Funcion anonima, es parecido a las funciones flecha en JS, 
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Obteniendo numeros pares en una lista
numeros_pares = list(filter(lambda numero: numero % 2 == 0, numeros))
print(numeros_pares)
# Obteniendo numeros impares en una lista
numeros_inpares = list(filter(lambda numero: numero % 2 == 1, numeros))
print(numeros_inpares)
#Retornando algo simple
retorno_simple = lambda nombre : f"hola {nombre} como estas?"
print(retorno_simple('querido'))
