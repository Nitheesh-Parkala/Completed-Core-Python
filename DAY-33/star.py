import re 

str="a python is ython but not pppython "
regex= r"p*ython"   #Its range is zero to infinity.[0-n...] 
#Output: ['python', 'ython', 'pppython']

res=re.findall(regex,str)
print(res)