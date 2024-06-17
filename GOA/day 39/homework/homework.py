#მომხმარებელს შემოატანინეთ ათი რიცხვი, ეს რიცხვები დაამატეთ სიაში, ამ სიიდან დაახარისხეთ ეს რიცხვები ორ ჯგუფად, რიცხვები რომლებიც მეტია 100 ზე და რიცხვები რომლებიც ნაკლებია 100 ზე

greater_than_100 = []
less_than_100 = []

for _ in range(10):
    number = input("Enter a number: ")

    if number > 100:
        greater_than_100 = greater_than_100 + [number]
    else:
        less_than_100 = less_than_100 + [number]


print("Numbers greater than 100:", greater_than_100)
print("Numbers less than or equal to 100:", less_than_100)
