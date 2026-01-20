#  1 - misol
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average(self):
        return sum(self.grades) / len(self.grades)

student = Student("Ali")
student.add_grade(90)
student.add_grade(80)

print("O‘rtacha:", student.average())


# 2 - misol
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average(self):
        return sum(self.grades) / len(self.grades)

student = Student("Ali")
student.add_grade(90)
student.add_grade(80)
student.add_grade(70)

print(student.name, "o‘rtacha bahosi:", student.average())


# 3 - misol
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def letter_grade(self):
        avg = sum(self.grades) / len(self.grades)
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        else:
            return "D"

student = Student("Vali", [85, 88, 90])
print("Harfli baho:", student.letter_grade())



# 4 - misol
class Group:
    def __init__(self):
        self.students = {}

    def add_student(self, name, grades):
        self.students[name] = grades

    def group_average(self):
        all_grades = []
        for grades in self.students.values():
            all_grades.extend(grades)
        return sum(all_grades) / len(all_grades)

group = Group()
group.add_student("Ali", [90, 80])
group.add_student("Vali", [70, 85])

print("Guruh o‘rtacha:", group.group_average())


# 5 - misol
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)

students = [
    Student("Ali", [90, 95, 92]),
    Student("Vali", [80, 85, 82]),
    Student("Sami", [70, 75, 78])
]

best = max(students, key=lambda s: s.average())
print("Eng yaxshi talaba:", best.name, best.average())


# 6 - misol
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            print("Baho 0–100 oralig‘ida bo‘lishi kerak")

student = Student("Ali")
student.add_grade(105)
student.add_grade(95)

print(student.grades)

