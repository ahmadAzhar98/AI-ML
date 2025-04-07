# There are four collection data types in python
# 1. List
# 2. Tuple
# 3. Set
# 4. Dictionary

# List
# List are ordered, changeable(mutable) and allow duplicate values


# List silicing 
my_list = ['p','r','o','g','r','a','m']
print("from index 2 to 5 items are", my_list[2:5])

count = my_list.count('r')
print("Count of r in my_list is", count)

# List comprehensions - concise way to create a list from another sequence in a single line
pow2 = [2 ** x for x in range(10) if x % 2 == 0 ]
print(pow2)

# Nested list or marix
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

print("Matrix : ",matrix[1][1:3])
print("Matrix : ",matrix[1:2][1:3]) # This not return 6,7 like the above [1:2] 
#will return list within list and second slice will also look for a list but since its not there it simply return []

# List operations : concatenation, repetition, membership
list1 = [1,2,3]
list2 = [4,5,6]
print("Concatenation of list1 and list2 is", list1 + list2)
print("Repetition of list1 is", list1 * 3)
print("Membership of 1 in list1 is", 1 in list1)

# Some methods 
list1.append(4)
print("Appended list1 is", list1)
list1.extend(list2)
print("Extended list1 is", list1)
list1.insert(2, 6)
print("Inserted list1 is", list1)
list1.remove(6)
print("Removed list1 is", list1)
