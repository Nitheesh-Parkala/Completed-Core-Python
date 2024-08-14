import re 

str="Python is a super language"
regex= r"super"

res=re.match(regex,str)
print(res)