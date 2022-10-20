birth_month = int(input("Введіть номер місяця (1-12) вашої дати народження: "))

date_of_birth = int(input("Введіть число вашої дати народження: "))

if birth_month > 12 or date_of_birth > 31 or birth_month <= 0 or date_of_birth <= 0:
    print("Ви ввели некоректну дату! ")
elif birth_month == 2 and date_of_birth >= 30:
    print("Ви ввели некоректну дату! ")
elif birth_month <= 2 and date_of_birth <= 20:
    print("Ваш знак зодіаку: Козоріг")
elif birth_month <= 2 and date_of_birth <= 18 or not birth_month >= 2:
    print("Ваш знак зодіаку: Водолій")
elif birth_month <= 3 and date_of_birth <= 20 or not birth_month >= 3:
    print("Ваш знак зодіаку: Риби")
elif birth_month <= 4 and date_of_birth <= 20 or not birth_month >= 4:
    print("Ваш знак зодіаку: Овен")
elif birth_month <= 5 and date_of_birth <= 21 or not birth_month >= 5:
    print("Ваш знак зодіаку: Телець")
elif birth_month <= 6 and date_of_birth <= 21 or not birth_month >= 6:
    print("Ваш знак зодіаку: Близнята")
elif birth_month <= 7 and date_of_birth <= 22 or not birth_month >= 7:
    print("Ваш знак зодіаку: Рак")
elif birth_month <= 8 and date_of_birth <= 22 or not birth_month >= 8:
    print("Ваш знак зодіаку: Лев")
elif birth_month <= 9 and date_of_birth <= 23 or not birth_month >= 9:
    print("Ваш знак зодіаку: Діва")
elif birth_month <= 10 and date_of_birth <= 23 or not birth_month >= 10:
    print("Ваш знак зодіаку: Терези")
elif birth_month <= 11 and date_of_birth <= 22 or not birth_month >= 11:
    print("Ваш знак зодіаку: Скорпіон")
elif birth_month <= 12 and date_of_birth <= 21 or not birth_month >= 12:
    print("Ваш знак зодіаку: Стрілець")









