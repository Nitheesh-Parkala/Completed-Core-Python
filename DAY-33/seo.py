import re 

str="Python is a super language"
regex= r"super"

res=re.search(regex,str)
print(res)