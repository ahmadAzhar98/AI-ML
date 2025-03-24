# Functions is a block of resuable code that performs a specific task. 

def greet():
    print("Hello, World!")
    
def greet(name):
    print("Hello, " + name + "!")
greet("Alice")    

def func(x):
    return x * 2

# A function is a resuable block of code for a specific task. In python functions are defined by they keyword def, followed by the name of the function and define the code in function body.
# While defining function values passed in the brackets are called parameters whereas while calling the function they are called arguments

from functools import partial

def multiply(x, y):
    return x * y

double = partial(multiply, 2)
print(double(3))

addition = lambda x, y: x + y
print(addition(2, 3))

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
factorial(5)

class Dog:
    def bark(self):
        return "Woof!"

def new_bark(self):
    return "Meow!"  

Dog.bark = new_bark  # Monkey patch in action

d = Dog()
print(d.bark()) 

#This is an important catch monkey patch is able to pull this off is because it is changing the code at runtime 
# because if it were at compile time, they compiler/interpreter would've have stopped the code.
