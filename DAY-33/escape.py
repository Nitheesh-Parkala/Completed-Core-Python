import re 

str="Python is a super language."
regex= r"\."

res=re.findall(regex,str)
print(res)