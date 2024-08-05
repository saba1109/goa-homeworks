# შექმენით ფუნქცია რომელშიც იქნება რიცხვებით სავსე სია და ფუნქცია დააბრუნებს ამ რიცხვების ჯამს
numbers = [1, 2, 3, 4, 5]
def sum_of_numbers():
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    print("The sum of the numbers is:", total)
sum_of_numbers()
