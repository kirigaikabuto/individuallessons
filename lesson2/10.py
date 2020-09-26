money = input('Сумма ипотеки:')
percent = input('ставка вознаграждения:')
years = input('Срок ипотеки:')
money_1 = int(money)
percent_1 = int(percent) / 100
years_1 = int(years)
total = money + ((money_1 * percent_1) * years_1)
total = f'total'
print(total)
