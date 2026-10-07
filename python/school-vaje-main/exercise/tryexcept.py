#1. Проверка ввода числа
#Напиши программу, которая: просит пользователя ввести число, если ввод некорректный — выводит сообщение если корректный — выводит квадрат числа
try:
    num= int(input("введите число :"))
    number = num ** 2
    print(f"ваше число в квадрате {number}")
except ValueError:
    print("число введено не верно")

# 2. Деление с обработкой ошибок
def safe_divide(a,b):
    try:
        divide= a/b
        print( f"разделенное число :{divide}")
    except ZeroDivisionError:
        print("на ноль делить нельзя")
    except ValueError:
        print("это не число")
a = int(input("число а:"))
b = int(input("число b:"))
safe_divide(a,b)

#3. Чтение файла с fallback
try:
    with open( "notes.txt", 'r', encoding='utf-8') as f:
        for i in f :
            print(i)
except FileNotFoundError:
    with open ( "notes.txt", 'w', encoding='utf-8') as f:
        f.write("файл создан")
        print("файл был создан, тк его не было ")

#Логирование ошибок
def errors ():
    try:
        tmp= input("введите выражение : ")
        result= eval(tmp)
        print(f"ваш результат: {result}")
    except  Exception as e:
        with open ( "errors.log", 'a', encoding="utf-8") as f:
            f.write(f" Ошибка : {type(e).__name__} - {e}\n")
        print("произошла ошибка")
errors()

#5. Преобразование списка

def numbers () :
    tmp= input("введите числа через запятую:")
    tmp= tmp.split(',')
    numberslist =[]
    errors=[]
    for i in tmp:
        i = i.strip()
        try:
            num=int(i)
            numberslist.append(num)
        except ValueError :
            errors.append(i)
    print("список чисел", numberslist)
    print("список ошибок", errors)
numbers()