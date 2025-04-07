# String is an array of 1 byte characters. 
# There are no characters just an string of size 1.
# Strings are immutable in python which means they cant not be modified

name = "Ahmad"
print(name)

# String interpolation is the 
# process of subsituting the value in placeholder in a string

# This is done with the help of f-string
age = 25
print(f"Name is {name} and age is {age}")

# String operations operations performed with the help of operator

# String concatenation
first_name = "Ahmad"
last_name = "Azhar"
full_name = first_name + " " + last_name
print("Full name is", full_name)

# String repetition
print("Repeating name 3 times", name * 3)

# String methods
print("Upper case name is", name.upper())
print("Lower case name is", name.lower())

# Escape characters

example = " He said \"how is the weather?\" "
print(example)