
# Task 15: Lambda, Map, Filter and Reduce

from functools import reduce

# Lambda
square = lambda x: x * x
print("Square of 5:", square(5))

# Map
numbers = [1, 2, 3, 4, 5]
mapped = list(map(lambda x: x * 2, numbers))
print("Map Result:", mapped)

# Filter
filtered = list(filter(lambda x: x % 2 == 0, numbers))
print("Filter Result:", filtered)

# Reduce
reduced = reduce(lambda x, y: x + y, numbers)
print("Reduce Result:", reduced)
