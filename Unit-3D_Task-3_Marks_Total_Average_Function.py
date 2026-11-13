
def calculate_marks(m1, m2, m3):
    total = m1 + m2 + m3
    average = total / 3
    return total, average

m1 = int(input("Enter first subject marks: "))
m2 = int(input("Enter second subject marks: "))
m3 = int(input("Enter third subject marks: "))

total, average = calculate_marks(m1, m2, m3)

print("Total Marks:", total)
print("Average Marks:", average)
