#DRY - Do Not Repeat Yourself

def greet(name):
    print(f"Hello, {name}")

def add(a, b):
    return a + b

def is_even(number):
    #Return True if number is even
    #Return False if number is odd

    # %
    #21/4 - 5.25 5 1/4

    if number % 2 == 0: return True
    else: return False


test1 = is_even(14)
test2 = is_even(39)
test3 = is_even(1)

print(test1)
print(test2)
print(test3)