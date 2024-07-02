# Enter a number to the user and then using a for loop output the sum of all the numbers up to this number (for example, if he enters 10, output the sum of all the numbers up to 10, for example).
num = int(input("Enter a number: "))

sum = 0

for i in range(num + 1):
    sum += i

print("The sum of all numbers up to", num, "is:", sum)