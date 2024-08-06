print("Enter a filename")
fname=input()

fptr=open(fname,"w")

for data in range(5):
    print("Enter a Name")
    name=input()
    fptr.write(name+ "\n")

fptr.close()
print("5 names written to file")