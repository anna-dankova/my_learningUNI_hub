#Пользователь вводит числа, пока не введёт 0.
#Программа должна:
#сохранить все числа в список
numbers=[]
while True:
    number=int(input("введите число: "))
    if number==0:
        break
    numbers.append(number)
#после выхода из цикла вывести: список. среднее арифметическое
print(numbers)
avg= sum(numbers)/len(numbers)
print(avg)