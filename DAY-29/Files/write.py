fptr1=open("DAY-29/Files/murnal.png","rb")
data=fptr1.read()

fptr2=open("new image.jpeg","wb")

fptr2.write(data)

fptr1.close()
fptr2.close()
print("New image is created")

