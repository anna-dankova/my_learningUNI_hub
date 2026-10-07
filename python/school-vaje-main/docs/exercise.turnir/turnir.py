
#считает количество учасников из одной страны. так же полное количество учасников
with open('Turnir.csv', 'r', encoding='utf-8') as file:
    lines = file.readlines()

    lines = lines[1:]
    country_counts = {}
    countries = []

for line in lines:
    line=line.strip()
    parts=line.split(';')
    country= parts[3].strip()
    countries.append(country)
    if country in country_counts:
        country_counts[country] +=1
    else:
        country_counts[country]=1
total=len(countries)


#считает сколько каждая странна получила вместе баллов
with open('Turnir.csv', 'r', encoding='utf-8') as file:
    lines = file.readlines()[1:]

country_elo_sums={}
for line in lines:
    line=line.strip()
    if not line:
        continue
    parts=line.split(';')
    country=parts[3].strip()
    elo_str=parts[4].strip()
    if elo_str.isdigit():
        elo=int(elo_str)
        if country in country_elo_sums:
            country_elo_sums[country] += elo
        else:
            country_elo_sums[country]= elo

#считает какая страна получила бошльше всего Эло баллов от одного учасника

with open('Turnir.csv', 'r', encoding='utf-8') as file:
    lines = file.readlines()[1:]
max_elo=0
max_country=[]
for line in lines:
    line = line.strip()
    if not line:
        continue
    parts = line.split(';')
    country = parts[3].strip()
    elo_points = parts[4].strip()
    elo_points=int(elo_points)
    if elo_points > max_elo:
        max_elo=elo_points
        max_country.append(country)

#считает сколько людей каждой категории и какие они

categories={}
for line in lines:
    line=line.strip()
    if not line:
        continue
    parts=line.split(';')
    cat=parts[6].strip()
    if cat:
        if cat in categories:
            categories[cat] += 1
        else:
            categories[cat]= 1

#считает сколько раз встречается каждое название

name={}
for line in lines:
    line=line.strip()
    if not line:
        continue
    parts=line.split(';')
    naziv=parts[0].strip()
    if naziv:
        if naziv in name:
            name[naziv] += 1
        else:
            name[naziv]= 1

print("Страны и их количество учасников:", country_counts)
print(f'Количество учасников вместе: {total}')
print("Сумма ELO по странам:", country_elo_sums)
print(f'Страна которая получила за раз больше всего баллов и сколько : {max_country}, {max_elo}')
print(f'Названия и количество учасников с ними : {name}')
print(f'Категории и количество учасников с ними : {categories}')




