 
def outer_function(text):
    msg = text

    def inner_functin():
        print(msg)

    return iner_function()

outer_function("Hello ...")