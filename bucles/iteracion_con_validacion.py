numeros = [3,4,5,6,1,2]
cadena = "Hola juancito"

#Iterando todos menos 1
for num in numeros:
    if num == 1:
        continue #Salta hacia el siguiente indice.
    print(num)
#Itera hasta que se cumpla la condicion 
for num in numeros:
    if num == 5:
        break   #Termina el bucle
    print(num) 
#Iterando Cadena de texto    
for letra in cadena:
    print(letra)