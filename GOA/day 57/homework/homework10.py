#Write a script with intentional errors and comment on why they occur.
def divide_numbers(a, b):
    # Dividing a number by zero is mathematically undefined
    # Python will raise a ZeroDivisionError when this happens
    return a / b
