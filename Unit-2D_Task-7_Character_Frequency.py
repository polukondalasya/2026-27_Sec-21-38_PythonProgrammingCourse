# Input string
text = input("Enter a string: ")

# Dictionary to store character frequencies
freq = {}

for char in text:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

# Display frequencies
print("Character Frequencies:")
for char, count in freq.items():
    print(f"'{char}' : {count}")