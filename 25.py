lista=[10,5,8,20,30]
k=lista[0]
for x in range (1,len(lista)):
    if lista[x]>k:
        k=lista[x]
print (k)
