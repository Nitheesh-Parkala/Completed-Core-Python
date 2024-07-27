a=[10,20,30,40,50,60]
a.remove(30)
print(a)

a.pop()
print(a)  #[10, 20, 40, 50]

a.pop(2)
print(a)  #[10, 20, 50]

print(a.index(20))  #1

a.clear()  
print(a)  #[]

# del a
print(a)  #Error

b=[10,20,10,30,10]
print(b.count(10))  #3
