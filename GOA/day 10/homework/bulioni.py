# მომხმარებელს შემოატანინეთ ორი ბულიან ტიპის მნიშვნელობა(true, false), შემდეგ კი დაბეჭდეთ ერკანზე ეს მნიშვნელობები      შედარებული ერთმანეთზე, ამისთვის გამოიყენეთ ლოგიკური ოპერატორები (and და or)
number1 = int(input("number1: "))
number2 = int(input("number2: "))
number3 = int(input("number3: "))

answer1 = number1<number2
answer2 = number2>number3

print(answer1 and answer2)
print(answer1 or answer2)