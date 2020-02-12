#acá armé el archivo de texto:

def carga():
    leer = open("diccionario.txt", "a")
    responde="si"
    dicc={}
    while responde=="si":
        ing=input("ingrese palabra en ingles: ")
        esp=input("ingrese su traducción al español: ")
        leer.write(ing + "=" + esp + "\n")
        dicc[ing]=esp
        responde=input("desea seguir cargando?(si/no)")
    leer.close()
    print(dicc)

def imprime(dicc):
    leer = open("diccionario.txt")
    for ing in dicc:
        print(ing,dic[esp])
diccionario=carga()
impresion=imprime(diccionario)
