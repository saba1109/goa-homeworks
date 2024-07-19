#შევქმნათ ცარიელი სია, მომხმარებელს შევეკითხოთ 1000 ჯერ თუ რისი დამატება სურს სიაში
user_list = []

for i in range(1000):
    user_input = input("Enter an item to add to the list: ")
    user_list.append(user_input)

print("Your list has been created with the following items:")
print(user_list)
