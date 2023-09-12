lista_animales = ["perro", "gatos", "loros", "ratones"]
lista_new_animales = ["nueva lista"]

# Estos bucles funcionan para listas y de la misma forma para tuplas tuplas_animal = (...,...,)
# y conjuntos set_animales = {...,...}

# Iterando con for
for animal in lista_animales:
    lista_new_animales.append(animal)

for animal in lista_new_animales:
    print(animal)
# Iterando con range
for num in range(10, 21):
    print(num)
# Iterando una lista con su indice
for animal in enumerate(lista_animales):
    index, value = animal  # Esta linea es como usar destructuring en JS.
    print(f'Indice =>{index} || Valor => {value}')
