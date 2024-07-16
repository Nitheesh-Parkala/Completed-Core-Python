#Handling the specific Exception
try:
    print("Enter a Value1")
    a=int(input())
    print("Enter a Value1")
    b=int(input())
    res=a/b
    print(res)
    
except (ValueError,ZeroDivisionError)  as e:
    print("It is A  ValueError or ZeroDivisionError")

# except ZeroDivisionError as e:
#     print("It is A ZeroDivisionError")

except Exception as e:
    print("It is A Error")