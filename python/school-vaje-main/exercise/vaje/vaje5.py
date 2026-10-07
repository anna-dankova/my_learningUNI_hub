delavci = [
    ("Tine", "Us",(1990, 5,33)),
    ("Tone","Novak",(1990,1,16)),
    ("Anton", "Novak",(1990,8,26)),
    ("Anton", "Novak",(1982,10,16)),
    ("Tine", "Us",(1990,15,6))
]
#Вывести всех работников построчно

for ime, priimek, (leto, mesec, dan) in delavci:
    print(f"{ime} {priimek} – {leto}-{mesec}-{dan}")

#Найти всех работников с фамилией "Novak"

novaki=[]
for delavec in delavci:
    if delavec[1]=="Novak":
        novaki.append(delavec)
print(novaki)

#Найти всех работников с именем "Anton"

antoni=[]
for delavec in delavci:
    if delavec[0]=="Anton":
        antoni.append(delavec)
print(antoni)

#Найти работников, родившихся после 1990 года

stari35inmanj=[]
for delavec in delavci:
    if delavec[2][0] ==1990:
        stari35inmanj.append(delavec)
print(stari35inmanj)

#Найти работников, у которых некорректная дата

narobedata=[]
narobemesec=[]
for delavec in delavci:
    if delavec[2][1] >12:
        print("erormounth ")
        narobemesec.append(delavec)
    elif delavec[2][2] >31:
        print("erordata")
        narobedata.append(delavec)
    else:
        print("data is okay")
print(f"ошибка в дате : {narobedata} . ошибка в месяце : {narobemesec}")

#Посчитать, сколько человек родилось в каждом году

starejsi=[]
mlajsi=[]
for delavec in delavci:
    if delavec[2][0]==1990:
        mlajsi.append(delavec[0:2])
    else:
        starejsi.append(delavec[0:2])
print(f"Те, кто родился в 1990: {mlajsi} (всего: {len(mlajsi)}), "
      f"а те, кто старше: {starejsi} (всего: {len(starejsi)})")

#Отсортировать работников по дате рождения
delavci = [
    ("Tine", "Us",(1990, 5,28)),
    ("Tone","Novak",(1990,1,16)),
    ("Anton", "Novak",(1990,8,26)),
    ("Anton", "Novak",(1981,10,16)),
    ("Tine", "Us",(1994,11,6))
]
sorted_bd=sorted(delavci, key=lambda  x: (x[2][0], x[2][1], x[2][2]))
print(sorted_bd)

#самый старший и младший

max_let = min(delavci, key=lambda x: x[2][0])
min_let = max(delavci, key=lambda x: x[2][0])
print(f"самый старший работник : {max_let}")
print(f"самый младший работник : {min_let}")