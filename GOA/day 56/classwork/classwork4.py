#4)დაწერეთ ალგორითმი, რომელიც მომხმარებელს შეეკითხება რიცხვს. თუ რიცხვი ლუწია გაყავით ორზე, სხვა შემთხვევაში გაამრავლეთ სამზე და მიუმატეთ ერთი.
number = int(input("type a number: "))
if number % 2 == 0:
    result = number // 2
else:
    result = number * 3 + 1

print(result)