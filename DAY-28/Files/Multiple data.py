print("Enter a filename")
fname=input()

fptr=open(fname,"w")

for data in range(2):
    print("Enter a Name")
    name=input()
    print("Enter a id")
    id=input()
    print("Enter a sal")
    sal=input()
    print("Enter a place")
    place=input()
    info= name +" "+id +" "+sal + " "+place
    fptr.write(info + "/n")

fptr.close()
print("2 names written to file")