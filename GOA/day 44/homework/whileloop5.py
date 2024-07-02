# Write a while loop that repeatedly asks the user to enter a password until the correct password "password123" is entered.

correct_password = "password123"
entered_password = ""

while entered_password != correct_password:
    entered_password = input("Enter the password: ")
    if entered_password != correct_password:
        print("Incorrect password. Please try again.")

print("Correct password entered. Access granted!")

