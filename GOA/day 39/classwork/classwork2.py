# მომხმარებელი შემოიტანს რიცხვს, შემდეგ კი თუ რიცხვი კენტია დაამატებთ კენტებისთვის განკუთვნილ სიაში
# თუ არადა ლუწებისთვის განკუთვნილ სიაში
odd_list = []
even_list = []


number = int(input("Enter a number: "))


if number % 2 == 0:
    even_list = even_list + [number]
else:
    odd_list = odd_list + [number]

# Print the lists
print("Odd list:", odd_list)
print("Even list:", even_list)