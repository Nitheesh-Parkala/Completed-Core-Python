def even(num):
    if(num%2==0):
        return True
    else:
        return False
    
L=[]
i=0
while(i<=4):
    print("Enter a Number")
    num=int(input())
    L.insert(i,num)
    i+=1
print(L)

i=0
while(i<=4):
    data=L[i]
    status=even(data)
    if(status==True):
        print(L[i])  #we can use print(data)
    i+=1

