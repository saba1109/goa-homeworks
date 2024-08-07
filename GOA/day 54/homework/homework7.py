#შექმენი ფუნქცია, რომელიც შემოატანინებს მომხარებელს რიცხვს და დააბრუნებს True, თუ ის ლუწია  და False, თუ არა.
def True_or_False():
    num = int(input("type any number: "))
    if num % 2 == 0:
        return "True"
    else:
        return "False"
print(True_or_False())