# Sets dont have duplicates, unordered colelection and mutable.
# Intialised using curly braces {}
s = {1,2,3,4,5}
s.add(6)
print(s)


# Set operations    
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print("Union of s1 and s2 is", s1.union(s2))
print("Intersection of s1 and s2 is", s1.intersection(s2))
print("Difference of s1 and s2 is", s1.difference(s2))

# Set methods
s1.add(6)
print("Added 6 in s1", s1)
s1.remove(6)
print("Removed 6 from s1", s1)
