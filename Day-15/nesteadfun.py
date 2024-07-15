def outer():
    print("Inside outer")

    def inner():
        print("Inside inner")
    inner()  #It should be always inside the outer function other wise it will throw error

outer()
