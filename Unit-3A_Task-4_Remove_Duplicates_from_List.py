# Original list
numbers = [10, 20, 30, 20, 40, 10, 50, 30]

# Remove duplicates
unique_numbers = []

for item in numbers:
    if item not in unique_numbers:
        unique_numbers.append(item)

print("Original List:", numbers)
print("List after removing duplicates:", unique_numbers)