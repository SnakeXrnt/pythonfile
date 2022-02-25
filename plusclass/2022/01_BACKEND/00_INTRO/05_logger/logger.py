

class Logger:

    def __init__(self,original_function):
        self.original_function = original_function

    def call(self,*args,**kwargs) :
        