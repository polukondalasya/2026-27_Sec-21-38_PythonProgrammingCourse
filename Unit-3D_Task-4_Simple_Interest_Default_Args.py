
def simple_interest(p, r=5, t=2):
    si = (p * r * t) / 100
    return si

p = float(input("Enter principal amount: "))

result = simple_interest(p)

print("Simple Interest:", result)
