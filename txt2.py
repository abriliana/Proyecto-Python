leer=open("archivo3.txt","a")
for x in range(2):
    dni=input("ingrese dni: ")
    ayn=input("ingrese apellido y nombre: ")
    leer.write(dni+","+ayn+"\n")
leer.close()
leer=open("archivo3.txt")
dicc={}
for x in leer:
    w=(x.strip())
    dni,ayn=w.split(",")
    dicc[dni]=ayn
print(dicc)
