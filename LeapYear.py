print('Введите год:')

leapYear = input()

if leapYear.isnumeric():
    leapYearInt = int(leapYear)

    if leapYearInt % 4 == 0 and (leapYearInt % 100 != 0 or leapYearInt % 400 == 0):
        print('Високосный год')
    else:
        print('Обычный год')
else:
    print('Год должен содержать только цифры!')