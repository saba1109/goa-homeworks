#მომხმარებელს შეეკითეთ სახელი, გვარი, ასაკი, საცხოვრებელი, შემდეგ შექმენით ფუნქცია რომელსაც არგუმენტად გადასცემთ ამ მონაცემებს და ეს ფუნქცია დააბრუნებს ერთ გრძელ წინადადებას მომხმარებლის შესახებ მაგ. hello {სახელი} {გვარი} შენ ცხოვრობ {საცხოვრებელი}
name = input("type your name: ")
surname = input("type your surname: ")
age = input("type your age: ")
location = input("type your adress: ")

def user_info(name, surname, age, location):
    return "Hello " + name + " " + surname + ", you are " + age + " years old and live in " + location + "."


print(user_info(name, surname, age, location))