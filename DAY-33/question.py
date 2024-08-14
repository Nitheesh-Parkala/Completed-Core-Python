import re 

str="a python is ython but not pppython "
regex= r"p?ython"   #Its range is zero to one. 
#Output: ['python', 'ython', 'python']

res=re.findall(regex,str)
print(res)