#შექმენით ფუნქცია რომელიც შეეკითხება მომხარებელს რიცხვს და დააბრუნებს ლუწია თუ კენტი
def even_or_odd():
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
print("The number is:",even_or_odd() )
