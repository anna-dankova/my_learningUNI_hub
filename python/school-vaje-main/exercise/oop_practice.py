import json
class Student :
    def __init__(self, name, age):
        self.name = name
        self.age=age
        self._grades =[]
        
    def introduce (self):
        return (f"My name is {self.name}")

    def add_grade(self,grade):
        if grade < 0 or grade > 100:
            raise ("Оценка не может быть негативной ")
        else :
            self._grades.append(grade)
    @property
    def average_grade (self):
        if not self._grades:
            return 0
        total=0
        for g in self._grades:
            total += g
        return total / len(self._grades)
    
    def __str__(self):
        return (f"Student: {self.name}, Age: {self.age} Avg: {self.average_grade}") 

    



class Group :
    def __init__(self):
        self.students=[]

    def add_student(self,student):
        self.students.append(student)

    def remove_student(self,name):
        for i, student in enumerate(self.students):
            if student.name == name:
                return self.students.pop(i)
        return None
    
    
    def found_student(self,name):
        for student in self.students:
            if  student.name == name:
                return student
        return None
    
    def group_average(self):
        if len(self.students) == 0:
            return 0
        
        total=0
        for student in self.students:
            total += student.average_grade
        return total/ len(self.students)
    
    def best_student(self):
        if len(self.students) == 0:
            return None
        
        best=None
        best_avg= -1

        for student in self.students:
            avg = student.average_grade
        
            if avg > best_avg:
                best_avg = avg
                best= student
        return best
        
    
    def print_all(self):
        for student in self.students:
            print(student)

    def save_to_file(self, filename):
        data =[]
        for s in self.students:
            s_dict = {
                'name': s.name,
                'age':s.age,
                'grades':s._grades,
                'type':s.__class__.__name__
            }
            if hasattr(s,'_class'):
                s_dict['_class']=s._class
            if hasattr(s,'_course'):
                s_dict['_course']=s._course
            data.append(s_dict)
        with open (filename, 'w', encoding='utf-8') as f:
            json.dump(data, f , ensure_ascii=False, indent=2)



class SchoolStudent(Student):
    def __init__(self, name, age,class_name):
        super().__init__(name, age)
        self._class=class_name

    def introduce(self):
        return (f"Привет, меня зовут {self.name}, я из {self._class} класса")



class UniversityStudent(Student):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course=course

    def introduce(self):
        return (f"Привет, меня зовут {self.name} , я на {self.course} курсе")


######
#test
# создаём группу
group = Group()

anna = Student("Anna", 20,2)
anna.add_grade(90); anna.add_grade(85) 

ivan = SchoolStudent("Ivan", 15, "10A")
ivan.add_grade(70); ivan.add_grade(60) 

kira = Student("Kira", 19 , 1)
kira.add_grade(90); kira.add_grade(80)

maria = UniversityStudent("Maria", 21, 2)
maria.add_grade(95)

group.add_student(anna); group.add_student(maria); group.add_student(kira); group.add_student(ivan)

best = group.best_student()
if best:
    print(f"🏆 {best.name} ({best.average_grade:.1f}): {best.introduce()}")
else:
    print("😔 Нет лидеров")



print(anna.average_grade) 
group.save_to_file('students.json')

##########