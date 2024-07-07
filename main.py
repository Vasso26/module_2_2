first = int (input('Введите первое число: '))
second = int (input('Введите второе число: '))
third = int (input('Введите третье число: '))
if first == second and second == third and first == third:
    print('Количество одинаковых чисел: 3')
elif first == second or second == third or first == third:
    print('Количество одинаковых чисел: 2')
else:
    print('Одинаковых чисел нет')