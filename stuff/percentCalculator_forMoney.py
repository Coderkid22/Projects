open("answers.txt", "w").close()

HST = 13

numbers = input('Questions : ')
pairs = numbers.split(',')
questionsList = {float(pair[0]): float(pair[1]) for pair in zip(pairs[::2], pairs[1::2])}

HSTorNot = input('Do you want to calculate tax?(13%)? ')

def percentage(percent, amount):
    return (percent * amount) / 100
answers = []
for item1_Price, item2_Price in questionsList.items():
    totalPrice = item1_Price + item2_Price
    tax = round(percentage(HST, totalPrice), 2)
    totalWithTax = round(totalPrice + tax, 2)
    # change = round(moneyUsed - totalWithTax, 2)
    with open("answers.txt", "a") as file:
       file.write(f'Subtotal : {totalPrice} | Taxes : {tax} | Total Cost : {totalWithTax}\n') 