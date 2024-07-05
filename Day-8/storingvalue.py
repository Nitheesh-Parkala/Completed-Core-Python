# Here a,b&c value 10 is stored on Ram and check weather it is same by using is.
a=10
b=10
c=10
g=[1,2]
h=[1,2]
print(a)
print(b)
print(c)
print(g is h) #False
print(id(a))
print(id(b))
print(id(c))

d=20
e=20
f=20
print(d)
print(e)
print(f)

print(id(d))
print(id(e))
print(id(f))

print(a is a) #True
print(a is b) #True
print(d is e) #True
print(a is d) #False
print(d is f) #True