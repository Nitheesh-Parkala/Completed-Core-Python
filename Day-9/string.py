str="RajaRamMohanRoy"

#Indexing....
print(len(str)) #15

print(str[0]) #R

print(str[14]) #y

print(str[-1]) #y

print(str[-8]) #M

#Slicing...
print(str[0:4]) #Raja

print(str[4:7]) #Ram

print(str[7:12]) #Mohan

print(str[12: ]) #Roy

print(str[ :7]) #RajaRam

print(str[7:]) #MohanRoy

print(str[4:0]) #No output

print(str[-8:-3]) #Mohan

print(str[-3:-8])

print(str[-3:-8:-1]) #Rnaho

print(str[2:10:3]) #jao

print(str[ :11:-1]) #yoR

print(str[5: :-1]) #aRajaR

print(str[-5: :-1]) #ahoMmaRajaR

print(str[-14: :2]) #aaaMhno

# print(str[4: 12: 0]) #Error

print(str[ : : -1]) #yoRnahoMmaRajaR (It also a reverse string)

print(str[ : : 3]) #RamhR

print(str[5: : 4]) #aho

print(str[-14: : -1]) #aR

print(str[8:1:-2]) #omRj
