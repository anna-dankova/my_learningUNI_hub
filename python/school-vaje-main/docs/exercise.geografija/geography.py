#Напиши функцию read_countries(filename), которая читает файл и возвращает список строк (без заголовка).

import csv
def read_countries_parsed(filename):
    with open(filename, 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader)
        return list(reader)
#Напиши функцию, которая считает количество стран в файле.
def count_countries(filename):
    with open (filename, 'r', encoding='utf-8-sig') as f:
        count_of_countries=0
        for i in countries_parsed:
            count_of_countries+=1
        return count_of_countries
#Выведи названия (Name) всех стран, относящихся к континенту Europe
def europe_countries(filename):
    europe=[]
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in countries_parsed:
            if line[4]=="Europe":
                europe.append(line[1])
        return europe
#найди страну с самой большой площадью
def biggest_surface_area(filename):
    max_area=0
    country_with_max_area=None

    for line in countries_parsed:
        area_str= line[5].strip().replace('.',"")
        if area_str:
            try:
                area=int(area_str)
                if area > max_area:
                    max_area= area
                    country_with_max_area= line[1]
            except ValueError:
                pass
    return max_area, country_with_max_area

#Подсчитай, сколько стран имеют неуказанный год независимости (IndepYear).
def independent_countries(filename):
    count=0
    for line in countries_parsed:
        if line[2] == '':
            count+=1
    return count

#Напиши функцию countries_by_continent(filename), которая возвращает словарь:
def countries_by_continent(filename):
    continents={
        "Africa" : [],
        "Europe": [],
        "Asia" : [],
        "North America" : [],
        "Oceania" : [],
        "Antarctica" : [],
        "South America" : []
    }
    for line in countries_parsed:
        name=line[1].strip()
        continent=line[4].strip()
        if continent in continents:
            continents[continent].append(name)
    for cont in continents:
        continents[cont].sort()

    return continents





if __name__=="__main__":
    filename="Geografija.csv"
    countries_parsed = read_countries_parsed(filename)
    for country in countries_parsed:
        print(f" Все страны : {country}")
    count=count_countries(filename)
    print(f" число стран : {count}")
    europe_countries=europe_countries(filename)
    print(f"страны Европы : {europe_countries}")
    biggest_coutry=biggest_surface_area(filename)
    print(f"Самая большая страна по площади : {biggest_coutry}")
    NotindeptCountries=independent_countries(filename)
    print( f"He независимых стран : {NotindeptCountries}")
    my_dict_continents=countries_by_continent(filename)

    print(f"Страны Африки:{my_dict_continents['Africa']}")
    print(f"Страны Азии:{my_dict_continents['Asia']}")
    print(f"Страны Антарктики:{my_dict_continents['Antarctica']}")
    print(f"Страны Океании:{my_dict_continents['Oceania']}")
    print(f"Страны Европы:{my_dict_continents['Europe']}")
    print(f"Страны Южной Америки:{my_dict_continents['South America']}")
    print(f"Страны Северной Америки:{my_dict_continents['North America']}")

