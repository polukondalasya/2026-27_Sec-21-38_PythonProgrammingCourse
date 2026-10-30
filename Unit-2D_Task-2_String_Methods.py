# Original string
text = "  Hello Python Programming  "

print("Original String:", text)

# upper()
print("Upper Case:", text.upper())

# lower()
print("Lower Case:", text.lower())

# strip()
print("After Strip:", text.strip())

# split()
words = text.strip().split()
print("After Split:", words)

# join()
joined_text = "-".join(words)
print("After Join:", joined_text)

# replace()
new_text = text.replace("Python", "Java")
print("After Replace:", new_text)

# find()
position = text.find("Python")
print("Position of 'Python':", position)