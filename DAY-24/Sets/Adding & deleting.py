a=set()

for i in range(5):
    print("Enter a value")
    data= int(input())
    a.add(data)
print(a)

a.update([6,7,8])
print(a)


print("Enter a Value to delete")
data1=int(input())

a.discard(data1)
print(a)

a.remove(5)
print(a)

a.clear()
print(a)
