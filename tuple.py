# Tuples are immuatable (cannot be changed)
# Tuples are faster than lists
# Tuples are intialised using () brackes.

my_tuple = (1,2,3,4,5)

# Different operations regarding tuples.
print("Tuple is", my_tuple)
print("Tuple slicing is", my_tuple[1:4])
print("Tuple repetition is", my_tuple * 2)
print("Tuple concatenation is", my_tuple + my_tuple)

# Mutiple data types in a tuple
my_tuple = (1,2.5,"Hello")

# Nested tuples
nested_tuple = ((1,2,3),(4,5,6),(7,8,9))

print("Nested tuple is", nested_tuple[1][:-1])