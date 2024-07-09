#String Interning

str1="rama"
str2="sita"
str3="ravana"
str4="rama"
str5="rama"
str6="sita"
str7="ravana"

print(id(str1))
print(id(str2))
print(id(str3))
print(id(str4))
print(id(str5))
print(id(str6))
print(id(str7))

print(str1)
print(str2)
print(str3)
print(str4)
print(str5)
print(str6)
print(str7)

#If same string is repeating like rama/sita/ravana It will not create separate memory map 
# instead of this it will identify the first memory map also ID will be same if the value is same 



