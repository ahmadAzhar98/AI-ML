# An iterator are used to tackle large data effiecently
my_list = [1, 2, 3, 4, 5]
my_iter = iter(my_list)
# print(next(my_iter))
# print(next(my_iter))

# Custom iterator
class PowTwo:
    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration

# numbers = PowTwo(10)
# i = iter(numbers)
# print(next(i))
# print(next(i)) 
# print(next(i))
# print(next(i))

# Python infinite iterators
from itertools import count
infinite_iterator = count(1)

for i in range(10):
    print(next(infinite_iterator))