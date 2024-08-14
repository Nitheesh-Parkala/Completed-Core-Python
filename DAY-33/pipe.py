import re 

str="Python is a super language."
regex= r"Python|super"

res=re.findall(regex,str)
print(res)