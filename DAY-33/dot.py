import re 

str="Python is a super language."
regex= r"."

res=re.search(regex,str)
print(res)