#გადმოგვეცემა რიცხვებით სავსე სია, ჩვენ ამ სიიდან უნდა შევკრიბოთ ყველა ხუთის ჯერადი რიცხვი და დავბეჭდოთ მათი ჯამი

numbers = [10, 23, 45, 55, 60, 78, 90, 100, 150, 3, 9]
sum_of_multiples = 0

for i in range(len(numbers)):
    if numbers[i] % 5 == 0:
        sum_of_multiples += numbers[i]

print(sum_of_multiples)
