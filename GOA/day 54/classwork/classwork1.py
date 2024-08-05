#შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება ორ რიცხვს და დააბრუნებს მათ ჯამს
def sum_of_two_numbers():
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    total = number1 + number2

    return total
result = sum_of_two_numbers()
print("The sum of the two numbers is:", result)
