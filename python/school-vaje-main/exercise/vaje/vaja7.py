with open("datoteka.txt", 'r', encoding="utf-8") as f:
    print(f.read())

with open("datoteka.txt", 'a', encoding="utf-8") as f:
    f.write("trying to learn python\n")
    f.write('first attempt')

with open("datoteka.txt", 'r', encoding="utf-8") as f:
    print(f.readline())
    print(len(f.read()))
    content=f.read()
    print(f'количество слов в файле: {len(content.split())}')
    print(f'количество букв в файле: {len(content)}')
    print(content[::-1])