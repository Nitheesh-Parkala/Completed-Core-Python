print("enter a value1")
a=int(input())

print("enter a value2")
b=int(input())

try:
    res=a/b
    print(res)
   
except Exception as e:
    print("Error in prg")
print("Prg End")