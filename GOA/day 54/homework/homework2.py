#შექმენი ფუნქცია, რომელიც შემოატანინებს მომხარებელს რიცვს და დააბრუნებს "მაგარია!", თუ რიცხვი 10-ზე მეტია.

def check_num ():
    num = int(input("type any number: "))
    if num > 10:
        return "magaria!"
    return ""
print(check_num())
