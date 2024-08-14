import re 

str="python is pyython but not pppyyyyyython "
regex= r"python$"   #Its range is zero to one. 
#Output: ['pyython']

res=re.findall(regex,str)
print(res)