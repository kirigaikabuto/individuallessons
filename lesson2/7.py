first_name = input("Введите имя:")
last_name = input("Введите фамилию:")
year = input("Введите ваш год рождения:")
full_name = first_name + " " + last_name
year_int = int(year)
age = 2020 - year_int
age_str = str(age)
print("Вас зовут " + full_name + " и ваш возраст " + age_str)


# Вас зовус ... и ваш возраст 22