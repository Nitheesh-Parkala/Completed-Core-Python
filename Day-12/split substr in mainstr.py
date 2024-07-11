#Finding a SubString in a Main String

str="If you think you can or you can't,you are right"
print(str)
print(str.count("you")) #4
str1="you"
print(str1 in str) #True

print(str.find("you")) #3
print(str.index("you")) #3
print(str.rfind("you")) #35
print(str.rindex("you")) #35
print(str.find("kohli")) #-1
print(str.index("Kohli"))