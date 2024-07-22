def outer():
    print("Entering Outer")

    def inner():
        print("Entering inner")
        print("processing")
        print("Leaving inner")
    print("calling inner")
    inner()
outer()
print("prg ended")