#A list in Python is an ordered collection of items, 
# which can be of any data type, and is defined by enclosing the items in square brackets. 
# Lists are mutable, meaning their elements can be changed after the list is created.
L=[]
i=0

while(i<=4):              #for i in range(i, 5): We can use this also.
    print("Enter a Number")
    num=int(input())
    L.insert(i,num)
    i+=1
print(L)