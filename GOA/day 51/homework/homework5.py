#  შექმენით სია რომელშიც იქნება 10 განსხვავებული რიცხვი შემდეგ კი დაბეჭდეთ ყველა ლისტის ელემენტის ჯამი
numbers = [2, 12, 8, 3, 9, 16, 3, 8, 10, 1]

sum = 0

for i in range(len(numbers)):
    sum += numbers[i]
print("The sum of all list elements is:", sum)
