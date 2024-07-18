L=[]
i=0

while(i<=4):
    print("Enter a Number")
    num= int(input())
    L.insert(i,num)
    i+=1

print(L)

k=list(filter(lambda num:num%2==0,L))
print(k)