from operator import index

ime=["Janez","Miha", "Ana", "Angela", "Rozi", "Matevz", "Pepca"]
visina=[ 1.88 , 1.91 , 1.65 , 1.77 , 1.71 , 1.75 , 1.80]
starost= [ 22, 23, 20, 21, 20, 21, 19]
#Найти самого высокого человека. Вывести его имя и рост.

max_height=max(visina)
index=visina.index(max_height)
print(f"самый высокий человек  {ime[index]} , рост  {visina[index]}см")

#Найти самого молодого человека. Вывести его имя и возраст.

min_age=min(starost)
index=starost.index(min_age)
print(f"самый младший человек  {ime[index]} , {starost[index]}   лет")

#Посчитать средний рост группы.Использовать циклы и/или функцию summ().

sredina=sum(visina)/len(visina)
print(f"средний рост :{sredina:.2f} cm")

#Посчитать средний возраст группы.

starostvseh=sum(starost)/len(starost)
print(f"средний возраст :{starostvseh:.0f}")

#Создать список людей старше 21 года. Вывести их имена.

for i in range(len(starost)):
    if starost[i]>21:
        print(f"{ime[i]} с возрастом {starost[i]} лет старше 21 года")

#Создать список людей выше 1.75 м. Вывести их имена и рост.

najvisji=[]
for name, height in zip(ime, visina):
    if height > 1.75:
        najvisji.append((name, height))
print(najvisji)

#добавить нового человека , имя , возраси и рост

ime.append("Tilen")
starost.append(22)
visina.append(1.85)
print(ime)

# сортировка роста и возраста
visinarev=visina.copy()
visinarev.sort(reverse=True)
print(visinarev)

starostrev=starost.copy()
starostrev.sort(reverse=True)
print(starostrev)

#Составить словарь {"имя": рост} для всех людей.

d=dict(zip(ime,visina ))
print(d)

#Найти человека, чей рост ближе всего к 1.80 м.Вывести его имя и рост.

target=1.80
razlike=[abs(v - target) for v in visina]
najblizji_index = razlike.index(min(razlike))
print(f"Ближе всех к {target} м: {ime[najblizji_index]}, рост {visina[najblizji_index]}")




