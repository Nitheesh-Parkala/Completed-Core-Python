# tell():  The tell() method returns the current position of the file pointer within the file. 
# The file pointer position is the location within the file where the next read or write operation will occur.


fptr=open("names.txt","r")
pos=fptr.tell()
print(pos)

data=fptr.read(3)
print(data)

pos= fptr.tell()
print(pos)

# seek(): The seek() method moves the file pointer to a specified position within the file. 
# This allows you to set the position from which to start the next read or write operation.

fptr.seek(3)
pos=fptr.tell()
print(pos)

data= fptr.read(5)
print(data)

