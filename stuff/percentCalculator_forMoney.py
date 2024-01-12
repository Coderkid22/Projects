HST = 13

numbers = input('Questions : ')
questionsList = list(map(float, numbers.split(',')))

HSTorNot = input('Do you want to calculate tax?(13%)? ')

def percentage(*percentAndAmount):
    percentAndAmount = list(percentAndAmount)
    return (percentAndAmount[0] * percentAndAmount[1]) / 100

for number in questionsList:
    Tax = percentage(HST, number)
    roundedTax = round(Tax, 2)
    roundedNumber = round(roundedTax + number, 2)
    print(f' Tax : {roundedTax} \n Total with tax : {roundedNumber}')