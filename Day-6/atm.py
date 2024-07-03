import datetime



print("Welcome to canara ATM")

print("Insert Your Card")

a=input()

if(a=="yes"):
    print("Enter Your 4 Digit Number")
    b=int(input())

    if(b==1234):
        print("Select Your Language: English, Kannada,Hindi")
        c=input().strip().capitalize()
    
        if c in ["English","Kannada","Hindi"]:
            print("Select Your Account: Saving ,current")
            d=input().strip().lower()

            if d in ["saving","current"]:
              print("Enter an Amount to withdraw")
              e=int(input())
              if(e>5000):
                 print("Pls check the balance")
              else:
                print("Processing...")
                print("Please collect the money")

                date = datetime.datetime.now()
                current_time = date.strftime("%Y-%m-%d %H:%M:%S")
                
                print("Pls Enter the name for receipt Bill")
                user_name=input().strip().capitalize()
                ##Receipt
                print("------Canara Bank Receipt-----")
                print("Name:"+ user_name)
                print("Date:"+ current_time)
                print("Amount Withdrawn:"+ str(e))
                print("----------****--------------")
                print("Thank You & Visit Again")
            else:
             print("Pls Select a proper account")
        else:
           print("Select Your Valid Language")
    else:
       print("Enter a valid pin")
else:
   print("Pls Insert Your card properly")


