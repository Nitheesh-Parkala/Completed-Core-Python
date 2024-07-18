def operation(data):
    return data+10

L=[]
i=0
while(i<=4):
    print("Enter a Value")
    a=int(input())
    L.insert(i,a)
    i+=1
k=list(map(operation,L))
print(k)

#Using lambda..
k=list(map(lambda data:data+10,L))
print(k)