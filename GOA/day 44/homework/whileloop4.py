#Write a while loop that processes a list of numbers, doubling each number, and prints the new list.
numbers = [1, 2, 3, 4, 5]
doubled_numbers = []
index = 0

while index < len(numbers):
    doubled_numbers.append(numbers[index] * 2)
    index += 1

print("Original list:", numbers)
print("Doubled list:", doubled_numbers)
