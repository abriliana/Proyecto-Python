def cargar():
    nombre=str(input("Ingrese nombre: "))
    sueldo=int(input("ingrese sueldo: "))
    return (nombre,sueldo)

def mayorsueldo(empleado1,empleado2):
    if empleado1[1]>empleado2[1]:
        print(empleado1[0],"tiene mayor sueldo")
    else:
        print(empleado2[0],"tiene mayor sueldo")


empleado1 = cargar()
empleado2 = cargar()
mayorsueldo(empleado1, empleado2)
