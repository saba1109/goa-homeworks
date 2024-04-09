#მომხარებელს შემოატანინეთ მშობლების ასაკი, დედის და მამის ასაკი, შემდეგ თუ დედის ასაკი მეტი იქნება მამის ასაკზე დაგვიბეჭდოს რომ დედა დიდი მამაზე თუ პირიქით მამის ასაკი მეტი იქნება დედის ასაკზე მაგ შემთხვევაში დაგვიბეჭდოს რომ მამა დიდია დედაზე. მინიშნება დაგჭირდებათ (if)

mom_age = int(input("type your mom's age: "))
dad_age = int(input("type your dad's age: "))

if mom_age > dad_age:
    print("your mom is older than your dad")


if dad_age > mom_age:
    print("your dad is older than your mom ")
