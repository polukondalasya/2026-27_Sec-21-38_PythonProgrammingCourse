
# Dictionary Methods

student = {
    "name": "Ravi",
    "age": 18,
    "branch": "CSE"
}

# Display dictionary
print("Dictionary:", student)

# Display keys
print("Keys:", student.keys())

# Display values
print("Values:", student.values())

# Display items
print("Items:", student.items())

# Add new item
student.update({"college": "ABC College"})
print("After Update:", student)

# Remove an item
student.pop("age")
print("After Pop:", student)

# Copy dictionary
new_student = student.copy()
print("Copied Dictionary:", new_student)

# Clear dictionary
student.clear()
print("After Clear:", student)
