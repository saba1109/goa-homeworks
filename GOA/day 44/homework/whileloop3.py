#Write a while loop that asks the user to guess a number between 1 and 10 until they get it right. The correct number is 7.
correct_number = 7
guess = 0

while guess != correct_number:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess != correct_number:
        print("Wrong guess. Try again!")

print("Congratulations! You guessed the correct number.")
