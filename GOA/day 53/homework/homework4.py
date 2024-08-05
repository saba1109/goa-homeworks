# შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება რიცხვს და შემდეგ კი დააბრუნებს დაბეჭდავს მომხმარებლის შემოტანილი რიცხვი კენტია თუ ლუწი
def odd_or_even():
    number = input("please enter any number: ")
    if number % 2 == 0:
        print("your selected number is even")
    else:
        print("your number is odd")

odd_or_even()