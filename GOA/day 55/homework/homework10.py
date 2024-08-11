#დაწერე ფუნქცია, რომელიც იღებს number პარამეტრს და აბრუნებს "კენტი" ან "ლუწი". მაგალითად, გამოიყენე არგუმენტი 8. (გამოიტანა: "ლუწი")
def odd_or_even(number):
    if number % 2 == 0:
        return "number is even"
    else:
        return "number is odd"
print(odd_or_even(10))