# The else block lets you execute code when there is no error
print("Enter a Value1")
a=int(input())
print("Enter a Value1")
b=int(input())

try:
    res=a/b
    print(res)
except Exception as e:
    print("It is A Error")
    print(e)
else:
    print("Prg Is Ended")