# Dictionaries are unordered, mutable have unique keys and heterogeneous
student_info = {
    'name': 'John',
    'age': 25,
    'course': 'Python'
}

# Dictionary operations
print("Student info is", student_info)
print("Student name is", student_info['name'])
print("Student age is", student_info.get('age'))

# Dictionary unpacking operations
d = {1: 'one', 2: 'two', 3: 'three'}
for key, val in d.items():
    print(key, val)

# Nested dictionary operations
nested_dict = {1: {'name': 'John', 'age': 25}, 2: {'name': 'Doe', 'age': 30}}
print("Nested dictionary is", nested_dict[1]['name'])
