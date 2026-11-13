 


balance = 1000

def deposit(amount):
    global balance
    balance = balance + amount
    print("Deposited Amount:", amount)
    print("Updated Balance:", balance)

def withdraw(amount):
    global balance
    balance = balance - amount
    print("Withdrawn Amount:", amount)
    print("Updated Balance:", balance)

# Main program
print("Initial Balance:", balance)

deposit(500)
withdraw(200)

print("Final Bank Balance:", balance)
                                                                                                                           