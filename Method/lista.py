lista = [1,2,3,4,5]

# Len Muestra la cantidad de elementos
print(len(lista))

#Apeend agrega al final 
lista.append("Jori")
print(lista)

#Insert agrega un elemento en un indice
lista.insert(2,"estoy en el indice 2")
print(lista)

#Inserta los elementos de una lista a otra lsta.
lista.extend(['1','Martes'])
print(lista)

#Pop elimina un elemento de la lista
lista.pop(1)
print(lista)
#Remove elimina un elemento de la lista, primero lo busca luego lo elimina.
lista.remove('Martes')
print(lista)
#Clear elimina la lista
lista.clear()
print(lista)

#Sort ordena de mayor a menor
lista.extend([4,5,2,1,64,0])
print(lista)
lista.sort()
print(lista)

#Reverse invierte la lista
lista.reverse()
print(lista)