def outer():
    print("Entering outer")

    def inner():
        print("Entering inner")
        print("Processing")
        print("Leaving inner")
    return inner
ref=outer()
print("calling inner function")
ref()
print("Prg ended...")