
count = 0

def increment():
    global count
    count = count + 1
    print("Counter =", count)

increment()
increment()
increment()

print("Final Counter =", count)
