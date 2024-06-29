#შევქმნათ სია რომელშიც გვექნება რომელშიც გვექნება დადებითი და უარყოფითი რიცხვები. გავფილტროთ, უნდა დავაბრუნოთ ორი სია ერთში მხოლოდ დადებითი რიცხვები მეორეში მხოლოდ უარყოფითი რიცხვები
numbers = [1, -2, 3, -4, 5, -6, 7, -8]

positive_numbers = []
negative_numbers = []

for i in range(len(numbers)):
    if numbers[i] > 0:
        positive_numbers.append(numbers[i])
    elif numbers[i] < 0:
        negative_numbers.append(numbers[i])

print("Positive numbers:", positive_numbers)
print("Negative numbers:", negative_numbers)

