#მომხმარებელს შეეკითხეთ სწავლობს თუარა გოაში, თუ სწავლობს შეეკითხეთ ომელ ჯგუფშია, თუ პასუხი იქნება ჯგუფი13 შეეკითეთ რომ არის თუ არა გაბრიელი მისი მენტორი, თუ პასუხი იქნება კი უთხარით რომ თქვენც აქ სწავლობთ და ნამდვილად გაბრიელია ორივეს მენტორი, თუ პასუხი არიქნება გაბრიელი ყველა სხვა შემთხვევაში დაუბეჭდეთ რომ ის ტყუის და არარის სინამდვილეში ჯგუფ13-ში if question_1 == "yes":

num1 = input("swavlob tuara goashi? :")

while num1 != "diax":
    num1 = input("swavlob tuara goashi? :")


if num1 == "diax":
    input("romel jgufshi xart? : ")

num2 = input("romel jgufshixart? :")

while num2 != 13:
    num2 = input("romel jgufshixart? :")

if num2 == 13:
    input("aris tuara gabrieli sheni mentori? :")

num3 = input("aris tuara gabrieli sheni mentori? :")

while num3 != "diax":
    num3 = input("aris tuara gabrieli sheni mentori? :")
    
if num3 == "diax":
    input("mec aq swavlob da namdvilad gabrielia chveni mentori :")
else:
    print("tyuixar shen ar xar jguf 13-shi")




