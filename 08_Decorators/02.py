

def display(func):
    def wrapper(*args,**kwargs):
        result = print(f"Function Name: {func.__name__} \n Params: {args,kwargs}")

        return result
    return wrapper


@display
def summ(a,b):
    return a + b

summ(45,69)