print("enter a filename")
fname=input()

fptr=open(fname,"r")

data=fptr.read()
print(data)  #It will print entire data from the file.

data=fptr.read(1)
print(data)  #It will print the specific number of line(bytes).

data=fptr.readline()
print(data)  #It will print  first single line from the file.

data=fptr.readlines()
print(data)   #It will print entire data in the list format.