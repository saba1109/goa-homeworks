#მომხმარებელს შემოვატანინოთ 10 რიცხვი შემდეგ დავამატოთ სიაში, გავფილტროთ ეს სია ორ ნაწილად ლუწებად და კენტებად და დავამატოთ ახალ სიაში ლუწები ცალკე კენტები ცალკე

numbers_list = []
even_numbers = []
odd_numbers = []
for i in range(10):
    user_numbers = int(input("enter number: "))
    numbers_list.append(user_numbers)

for i in range(len(numbers_list)):
    if numbers_list[i] % 2 == 0:
        even_numbers.append(list[i])
    else:
        odd_numbers.append(list[i])
print("this is even numbers: ", even_numbers)
print("this is odd numbers: ", odd_numbers)