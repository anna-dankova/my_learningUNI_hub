
try:
    num = int(input('введите натуральное число: '))
    if num <= 0:
        raise ValueError("Число должно быть натуральным (больше 0)")
except ValueError as e:
    print('Ошибка ввода:', e)
else:
    print('Вы ввели:', num)
finally:
    print('Проверка натурального числа завершена')
