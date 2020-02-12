eq=0
es=0
iso=0
l=int(input("ingrese cantidad de triangulos: "))
for c in range (l):
    l1=int(input("ingrese valor: "))
    l2=int(input("ingrese valor: "))
    l3=int(input("ingrese valor: "))
if l1==l2 and l2==l3:
    eq=eq+1
    else:
        if l1==l2 or l2==l3 or l1==l3:
            iso=iso+1
        else:
            es=es+1
print(iso, es, eq)
