print("Enter a str1")
str1=input()

print("Enter a str2")
str2=input()

if(str1>str2):    #c1: str1=ramu & str2=rama
    print("str1 is grt")
elif(str2>str1):  #c1: str1=rama & str2=ramu
    print("str2 is grt")
else:             #c3: str1=rama & str2=rama
    print("str1==str2")

#Case1: str1=ramu & str2=rama
# 114 97 109 117
# 114 97 109 97
#---------------
#  0  0   0  20

#Case2: str1=rama & str2=ramu
# 114 97 109 97
# 114 97 109 117
#---------------
#  0  0   0  -20

#Case3:  str1=rama & str2=rama
# 114 97 109 97
# 114 97 109 97
#---------------
#  0  0   0  0
