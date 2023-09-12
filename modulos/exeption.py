def numeros(numero):
    try:
        numero = int(numero)*2
        return numero
        """ raise """ #Podemos lanzar exepciones
    except ValueError as e:
        print(f"Lo que ingresaste no fue un numero")
        print(f"{e}") 