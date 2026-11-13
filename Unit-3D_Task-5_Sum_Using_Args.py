
def sum_numbers(*args):
    total = 0
    for n in args:
        total = total + n
    return total

result = sum_numbers(10, 20, 30, 40)

print("Sum:", result)
