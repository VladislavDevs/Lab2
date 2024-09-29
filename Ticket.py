print('Введите номер билета:')

ticketNumber = input()

if ticketNumber.isnumeric() and len(ticketNumber) == 6:
    numbers = [int(i) for i in ticketNumber]

    if sum(numbers[3:]) == sum(numbers[:3]):
        print('Счастливый билет')
    else:
        print('Несчастливый билет')
else:
    print('Год должен содержать только цифры и количество цифр, должно быть - 6!')