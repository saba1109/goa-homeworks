# შექმენი ფუნქცია, რომელიც შემოატანინებს მომხარებელს ორ რიცხვს და დააბრუნებს მათ ჯამს დამატებული 5.
def sum_plus_five():
    num1 = int(input("type any number: "))
    num2 = int(input("type any number again: "))
    sum = num1 + num2
    return sum + 5
print("sum of numbers + five is",sum_plus_five())
