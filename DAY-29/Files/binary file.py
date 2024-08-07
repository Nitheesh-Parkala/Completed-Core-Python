fptr =open(r"DAY-29/Files/murnal.png","rb")  #u can prefix the string with r to treat it as a raw string, which will ignore escape sequences:
data=fptr.read()
print(data)
