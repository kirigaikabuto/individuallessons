# входные данные
hour = input("Введите ваш оклад за час:")
time_in_day = input("Cколько часов в день вы работаете:")
days = input("Введите колво рабочих дней:")
day_off = input("Введите колво пропусков:")
tax = 0.1
# преобразование данных в нужны формат
hour1 = int(hour)
days1 = int(days)
day_off1 = int(day_off)
time_in_day1 = int(time_in_day)
# подсчет по формуле или реализация бизнес логики
day_profit = hour1 * time_in_day1
print("Оклад за день:", day_profit)
real_work_day = days1 - day_off1
print("Количество дней которые работал:", real_work_day)
month_profit = day_profit * real_work_day
print("Зарплата за месяц:", month_profit)