
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

print_details(name="Lasya", age=18, branch="CSE Cyber")
