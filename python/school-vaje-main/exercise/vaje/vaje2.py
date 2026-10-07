#считает от 0  до 10
i=0
while i<10:
    i+=1
    print(i)

#считает от 1 до n числа
n=int(input("number : "))
i=0
while i<n:
    i+=1
    print(i)

#выводит четные числа
numbers=[1,2,3,4,5,6,7,8,9,10]
for i in numbers:
    if i%2==0:
        print(i)

#  находит большее число в списке
num=[3,54,22,57,1,14,26,24]
max=1
for i in num:
    if i>max:
        max=i
print(max)

#переворачивает список

lst=[1,2,3,4,5]
lst.reverse()
print(lst)

# найти все буквы а в строке

text="abarakadabra"
count=0
for i in text:
    if i=="a":
        count+=1
print(count)

