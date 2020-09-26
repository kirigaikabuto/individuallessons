first_name = input("Введите имя:")
last_name = input("Введите фамилию:")
year = input("Введите ваш год рождения:")
full_name = first_name + " " + last_name
year_int = int(year)
age = 2020 - year_int
output = f"Вас зовут {full_name} и ваш возраст {age}"
print(output)