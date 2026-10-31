# Python program to demonstrate set membership testing
# and set methods: add(), remove(), discard()

# Creating a set
numbers = {10, 20, 30, 40}

print("Original Set:", numbers)

# Membership Testing
print("\nMembership Testing:")
print("20 in set?", 20 in numbers)
print("50 in set?", 50 in numbers)

# Adding an element
numbers.add(50)
print("\nAfter adding 50:", numbers)

# Removing an element
numbers.remove(20)
print("After removing 20:", numbers)

# Discarding an element
numbers.discard(30)
print("After discarding 30:", numbers)

# Discarding an element that does not exist
numbers.discard(100)  # No error occurs
print("After discarding 100:", numbers)