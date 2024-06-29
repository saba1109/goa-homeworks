#მომხმარებელს შემოატანინეთ ათი რიცხვი, ეს რიცხვები დაამატეთ სიაში, ამ სიიდან დაახარისხეთ ეს რიცხვები ორ ჯგუფად, რიცხვები რომლებიც მეტია 100 ზე და რიცხვები რომლებიც ნაკლებია 100 ზე

numbers = []
more = []
less = []
for i in range(10):
    users_input = int(input("please enter number: "))
    numbers.append(users_input)

for i in range(len(numbers)):
    if numbers[i] == 100:
        continue
    elif numbers[i] > 100:
        more.append(numbers[i])
    else:
        less.append(numbers[i])
print("this numbers are more than 100: ", more)
print("this numbers are less than 100: ", less)