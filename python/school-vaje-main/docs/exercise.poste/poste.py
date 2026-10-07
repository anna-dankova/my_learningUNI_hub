#1215 Medvode
#1216 Smlednik
#1217 Vodice

with open ('poste.txt', 'r', encoding='utf-8') as f:

    count_of_1 = 0
    count_of_2 = 0
    count_of_3 = 0
    count_of_4 = 0
    count_of_5 = 0
    count_of_6 = 0
    count_of_7 = 0
    count_of_8 = 0
    count_of_9 = 0

    for line in f:
        line=line.strip()
        if line:
            try:
                first_digit=line.split()[0][0]
                if first_digit == '1':
                    count_of_1 += 1
                elif first_digit == '2':
                    count_of_2 += 1
                elif first_digit == '3':
                    count_of_3 += 1
                elif first_digit == '4':
                    count_of_4 += 1
                elif first_digit == '5':
                    count_of_5 += 1
                elif first_digit == '6':
                    count_of_6 += 1
                elif first_digit == '7':
                    count_of_7 += 1
                elif first_digit == '8':
                    count_of_8 += 1
                elif first_digit == '9':
                    count_of_9 += 1
            except (IndexError, ValueError):
                print(f"Пропущена строка с ошибкой: {line}")


print("Счётчики по первой цифре номера почты:")

print(f"1: {count_of_1}")
print(f"2: {count_of_2}")
print(f"3: {count_of_3}")
print(f"4: {count_of_4}")
print(f"5: {count_of_5}")
print(f"6: {count_of_6}")
print(f"7: {count_of_7}")
print(f"8: {count_of_8}")
print(f"9: {count_of_9}")

counts={ '1':90, '2': 98,'3':64, '4': 45, '5':43, '6': 38, '7':0, '8':62, '9':36}
max_digit=max(counts,key=counts.get)
max_value=counts[max_digit]
print(f"Больше всего: цифра {max_digit} ({max_value} раз)")

with open ('poste.txt', 'r', encoding='utf-8') as f:
    count_of_f=0
    for line in f:
        line = line.strip()
        if line[5] == 'P':
            count_of_f+=1
print(count_of_f)

with open ('poste.txt', 'r', encoding='utf-8') as f:
    count_of_words=0
    for line in f:
        line = line.strip()
        if line:
            parts = line.split()
            if len(parts)>=3:
                name_parts=parts[1:]
                if len(name_parts)==2:
                    count_of_words+=1
print(count_of_words)