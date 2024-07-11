print("Enter A String")
str = input()
i=0
newStr = " "
while(i<=len(str)-1):
    data = str[i]
    if(data == " "):
        i+=1
    else:
        newStr+=data
        i+=1
print(newStr)