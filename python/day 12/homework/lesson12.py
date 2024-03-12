#მომხმარებელს შემოატანინეთ ტესტში მიღებული ქულა, თუ ქულა მეტია 90 - ზე და ნაკლებია 100 - ზე მაგ შემთხვევაში დაპრინტეთ, თქვენ დაგიფინანსდებათ სწავლა სრულიად. თუ მიღებული ქულა მეტია 70 - ზე და  ნაკლებია 80 - ზე მაგ შემთხვევაში დაპრინტეთ, თქვენ დაგიფინანსდებათ სწავლა 1500 ლარით, თუ მიღებული ქულა მეტია 40 -  ზე და ნაკლებია 70 - ზე მაგ შემთხვევაში დაპრინტეთ, თქვენ დაგიფინანსდებათ სწავლა 500 ლარტით, ხოლო თუ მიღებული ქულა ნაკლებია 40 ზე, მაგ შემტხვევაში დაპრინტეთ, ტქვენ არ დაგიფინანსდებათ სწავლის პროცესი 


score = int(input("enter your test core"))

if score > 90 and score < 100:
    print("Congratulations! You will be financed for your studies.")

elif score > 70 and score < 80:
    print("you will be financed with 1500gel for study")

elif score > 40 and score < 70:
    print("you will be financed with 500gel for study")

elif score < 40:
    print("you will not be financed for study")


