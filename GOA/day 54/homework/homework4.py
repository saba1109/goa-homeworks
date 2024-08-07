# შექმენი ფუნქცია, რომელიც შემოატანინებს მომხარებელს ტექსტს და დააბრუნებს ტექსტის სიგრძეს.
def len_text():
    text = input("write a text: ")
    return len(text)
print("the size of text is",len_text())