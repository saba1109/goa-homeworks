#შექმნი ფუნქცია, რომელიც იღებს number პარამეტრს და აბრუნებს "დიდია" თუ number 10-ზე მეტია და "პატარა" თუ ნაკლებია. მაგალითად, გამოიყენე არგუმენტი 9. (გამოიტანა: "პატარა")
def big_small(number):
    if number > 10:
        return "big"
    else:
        return "small"
print(big_small(15))