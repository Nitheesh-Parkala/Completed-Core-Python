a=[]
i=0

while(True):
    print("enter a Value")
    num = int(input())
    a.insert(i,num)
    i+= 1

    print("Do you wish to Continue")
    print("Press 1: Yes")
    print("Press 2: No")

    choice = int(input())
    if(choice == 1):
      continue
    else:
      break
print(a)
print("Prg End")