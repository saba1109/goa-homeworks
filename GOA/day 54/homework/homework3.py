#შექმენი ფუნქცია, რომელიც შემოატანინებს მომხარებელს ორ ციფრს და დააბრუნებს მათ შორის უმცირესს.
def input_nums ():
    num1 = int(input("type first number: "))
    num2 = int(input("now type second number: "))
    if num1 > num2:
        return "second number is the smaller"
    elif num1 < num2:
        return "first number is the smaller"
    else:
        return "The numbers are equal to each other"
print(input_nums())