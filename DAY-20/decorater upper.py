def print_msg():
    str="Hello EveryOne"
    return str
def outer(print1):
    print("Entering the outer")

    def inner():
        print("Entering the inner")
        ref=print1
        str1=ref()
        str2=str1.upper()
        print(str2)
    return inner

ptr1=print_msg
ptr2=outer(ptr1)
ptr2()