# Выведи все положительные числа
nums = [3, 7, -2, 8, 0, -5, 10]
for a in nums:
    if a >0:
        print(a)
# Найди сумму всех элементов
total=0
for a in nums:
    total+=a
print(total)

# Найди максимальный элемент без max()
# 👉 Используй for
maxnum=0
for a in nums:
    if a > maxnum:
        maxnum=a
print(maxnum)