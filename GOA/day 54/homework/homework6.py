# შექმენი ფუნქცია, რომელიც შემოატანინებს მომხარებელს რიცხვს და თუ ის დადებითი იქნება, დააბრუნებს "დადებითი", და თუ უარყოფითი იქნება, "უარყოფითი".
def positive_or_negative ():
    num = int(input("type a number: "))
    if num < 0:
        return "number is negative"
    elif num > 0:
        return "number is positive"
    else:
        return "number is 0"
print(positive_or_negative())