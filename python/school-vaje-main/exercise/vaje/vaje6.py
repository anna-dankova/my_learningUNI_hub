
tekmovalci = {
    "Ana": {
        "stevilka": 1,
        "plavanje": 30,
        "kolesarjenje": 90,
        "tek": 45
    },
    "Bine": {
        "stevilka": 2,
        "plavanje": 25,
        "kolesarjenje": 95,
        "tek": 50
    },
    "Cilka": {
        "stevilka": 3,
        "plavanje": 28,
        "kolesarjenje": 85,
        "tek": 48
    },
    "Domen": {
        "stevilka": 4,
        "plavanje": 33,
        "kolesarjenje": 88,
        "tek": 46
    },
    "Eva": {
        "stevilka": 5,
        "plavanje": 29,
        "kolesarjenje": 92,
        "tek": 47
    }

}
#тут короче персон это  как ключ , имя короче. инфо это значения ключа. и мы ищем значения в текмовалци. и печатает в каждом ключе значение под именем штевилка
#Выведи всех участников и их номера.
for person, info in tekmovalci.items():
    print(person ,info["stevilka"])

#Выведи время плавания для каждого участника.
print("cas plavanja in imena :")
for person, info in tekmovalci.items():
    print(person, info["plavanje"])

#Найди участника с минимальным временем на плавание.
casplavanja=[]
for person, info in tekmovalci.items():
    casplavanja.append(info["plavanje"])
print(f"минимальное время плаванья : {min(casplavanja)}")

#Посчитай среднее время бега для всех участников.
casteka=[]
for person, info in tekmovalci.items():
    casteka.append(info["tek"])
print(f"среднее время бега :  {sum(casteka)/len(casteka)}")

#Выведи имя участника с наибольшим временем на вело.
maxvelo=0
winner=""
for person, info in tekmovalci.items():
    if info["kolesarjenje"] > maxvelo:
        maxvelo = info["kolesarjenje"]
        winner = person
print(f"Участник с наибольшим временем на вело: {winner}, время: {maxvelo}")



#


#


#


#


#


#


#


#


#


