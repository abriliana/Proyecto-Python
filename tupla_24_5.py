#definir una tupla con 3 valores enteros, convertir el contenido de la tupla a lista, modificar la lista y luego volver  aconvertir en tupla.
tupla=(2,5,10)
lista=list(tupla)
lista.append(30)
nuevatupla=tuple(lista)
print(nuevatupla)