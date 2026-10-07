def read_numbers(filename):
    number=[]
    with open(filename, "r", encoding="utf-8") as f :
        for i in f:
            cleaned=i.strip()
            if cleaned:
                number.append(int(cleaned))
    return number

def sum_numbers(numbers):
    total=0
    for num in numbers:
        total+=num
    return total

def print_numbers(numbers):
    for i in numbers:
        print(i)

def squares_of_num_and_save(numbers):
    with open("squares.txt", "w", encoding="utf-8")as f:
        sqrts=[]
        for i in nums:
            sqrts.append(int(i**2))
            f.write(str(sqrts) + "\n")
        return sqrts

def fruits_read(file):
    count = 0
    with open ( file,"r", encoding="utf-8") as f :
        for i in f:
            cleaned=i.strip()
            if cleaned:
                count+=1
        return count

def fruits_count(count):
    print(f" в этом файле {count} фруктов ")

def new_fruit(file, new_word):
    with open( file, "a",encoding="utf-8") as f:
        f.write(new_word + "\n")
    return f"Слово '{new_word}' добавлено в {filename}"


if __name__=="__main__":
    filename= "numbers.txt"
    nums=read_numbers(filename)
    print_numbers(nums)
    summ=sum_numbers(nums)
    print(summ)

    squares=squares_of_num_and_save(nums)
    print(squares)

    file= "fruits.txt"
    counted= fruits_read(file)
    fruits_count(counted)
    new_word="pineapple"
    result=new_fruit(file,new_word)
    print(result)




