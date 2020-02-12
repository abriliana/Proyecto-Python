leer=open("archivo2.txt","a")
for x in range(2):
    dni=input("ingrese dni: ")
    ayn=input("ingrese apellido y nombre: ")
    leer.write(dni+","+ayn+"\n")
leer.close()
leer=open("archivo2.txt")
lista=[]
for x in leer:
    w=(x.strip())
    d=w.split(",")
    lista.append(d)
    print(lista)
leer.close()
