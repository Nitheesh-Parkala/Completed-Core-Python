#filter is used when we want to filter the item to obtain required value.
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

#filter
k= list(filter(even,L))
print(k)