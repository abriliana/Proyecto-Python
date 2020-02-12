def cargar():
    lista=[]
    for x in range(3):
        v=int(input("Ingrese valor: "))
        lista.append(v)
    return lista

def retornar_mayormenor(lista):
    may=lista[0]
    men=lista[0]
    for x in range(1,len(lista)):
        if lista[x]>may:
            may=lista[x]
        else:
            if lista[x]<men:
                men=lista[x]
    return (may,men)


lista=cargar()
mayor,menor=retornar_mayormenor(lista)
print("El mayor es: ",ma)
#Hacer 3 funciones:  1-lista de 5 enteros. 2-retornar el mayor y el menor de la lista emdiante tupla. 3-desempaquetar la tupla en el bloque principal y mostrr el menor y el mayor.
