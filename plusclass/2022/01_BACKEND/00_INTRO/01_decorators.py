
def decorator_function(original_function):

    def wrapper_function(*args, **kwargs):
        print('wrapper executed before {}'.format(original_function.__name__))
        return original_function(*args,**kwargs)

    return original_function()

@decorator_function
def display():
    print('display function ran well.')
    
@decorator_function
def display_info(name,age):
    print(f"display_indo ran with arguments ({name},{age}")

display()
display_info("kevin",28)