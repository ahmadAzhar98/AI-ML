# First class objects
def say_hello(name):
    return f"Hello {name}"

def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def greet_ahmad(greeter_func):
    return greeter_func("Ahmad")

print(greet_ahmad(say_hello))
print(greet_ahmad(be_awesome))

# Inner functions
def parent(num):
    def first_child():
        return "Hi, I am greatest player of all time"

    def second_child():
        return "I am the greatest player of my age"

    if num == 1:
        return first_child
    else:
        return second_child
    
first = parent(1)
second = parent(2)
print(first())
print(second())