def print_msg():
    print("Hello Everyone")

def outer(print1):
    print("Entering outer")

    def inner():
        print("Entering inner")
        ref =print1
        ref()
        print("Leaving inner")
    return inner
ptr1=print_msg
ptr2=outer(ptr1)
ptr2()
print("prg ended...")