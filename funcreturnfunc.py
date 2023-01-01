def outer_func():
    def inner_func():
        print("inside inner func")
    return inner_func
var=outer_func()
var()
