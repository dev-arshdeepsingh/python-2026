# Decorators aren't advance topics
# Works like a toll booth like charges of car, truck are different even if for 2 wheelers it's free but still they have to go through the toll booth.
# lly, every func. has to go via toll booth called decorator

#Problem 1: Write a decorator a that measures time that func takes to executes

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f"{func.__name__} executed in {end - start} time")
        return result
    
    return wrapper


@timer
def demo(n):
    time.sleep(n)

demo(2)
demo(5)

#Decorators are also functions which has wrapper func. that execute every func & return their execution as result. 
#Decorator returns wrapper function definition