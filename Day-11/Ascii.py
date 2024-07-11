# Write a Prg to Convert LowerCase To upperCase  and UpperCase to LowerCase letter without using the InBuilt Function.
print("Enter The String")
str= input()
i=0
newStr=""

while(i<= len(str)-1):
    data=str[i]
    ascii_val=ord(data)
    if(ascii_val>=97 and ascii_val<=122):
       char= ascii_val-32
       newChar=chr(char)
       newStr = newStr+newChar
    else:
       char= ascii_val+32
       newChar=chr(char)
       newStr = newStr+newChar
    i+=1
print("Converted string", newStr)
       