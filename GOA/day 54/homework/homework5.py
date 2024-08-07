# შექმენი ფუნქცია, რომელიც შემოატანინებს მომხარებელს ორ რიცხვს და დააბრუნებს მათ ჯამს.
def sum_of_numbers ():
    num1 = int(input("type a number: "))
    num2 = int(input("type second number: "))
    sum = num1 + num2
    return sum
print("sum of your numbers is", sum_of_numbers())