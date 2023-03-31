class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    """Метод выставления оценок лекторам от студентов"""

    def rate_lector(self, lector, course, grade):
        if (
            isinstance(lector, Lecturer)
            and len(set(self.courses_in_progress) & set(lector.courses_attached)) != 0
        ):
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            raise ValueError("Неправильное заполнение данных!")

    """Метод расчета средней оценки"""

    def average_rating(self, dic):
        sum = 0
        count = 0

        for m in dic.values():
            for i in m:
                sum += i
                count += 1
        if count == 0:
            return 0
        else:
            return round(sum / count, 1)

    """Метод сравнения студента с лектором"""

    def __eq__(self, value):
        if isinstance(value, Mentor):
            check = value.average_rating(value.grades)
            print(self.average_rating(self.grades) == check)
        else:
            print('Студент должен сравниваться с лектором!')

    def __lt__(self, value):
        if isinstance(value, Mentor):
            check = value.average_rating(value.grades)
            print(self.average_rating(self.grades) < check)
        else:
            print('Студент должен сравниваться с лектором!')

    def __le__(self, value):
        if isinstance(value, Mentor):
            check = value.average_rating(value.grades)
            print(self.average_rating(self.grades) <= check)
        else:
            print('Студент должен сравниваться с лектором!')

    def __gt__(self, value):
        if isinstance(value, Mentor):
            check = value.average_rating(value.grades)
            print(self.average_rating(self.grades) > check)
        else:
            print('Студент должен сравниваться с лектором!')

    def __ge__(self, value):
        if isinstance(value, Mentor):
            check = value.average_rating(value.grades)
            print(self.average_rating(self.grades) >= check)
        else:
            print('Студент должен сравниваться с лектором!')

    def __str__(self):
        average = self.average_rating(self.grades)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    """Метод расчета средней оценки"""

    def average_rating(self, dic):
        sum = 0
        count = 0

        for m in dic.values():
            for i in m:
                sum += i
                count += 1
        if count == 0:
            return 0
        else:
            return round(sum / count, 1)

    def __str__(self):
        average = self.average_rating(self.grades)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average}"


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

    """Метод выставления оценок студентам от ревьювера"""

    def rate_student(self, student, course, grade):
        if (
            isinstance(student, Student)
            and course in self.courses_attached
            and course in student.courses_in_progress
        ):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            raise ValueError("Неправильное заполнение данных!")


student_Masha = Student("Мария", "Уткина", "Женщина")
student_Masha.courses_in_progress += ["Python"]
student_Masha.courses_in_progress += ["Git"]

student_Yura = Student("Юрий", "Холодов", "Мужчина")
student_Yura.courses_in_progress += ["Python"]
student_Yura.courses_in_progress += ["JS"]
student_Yura.finished_courses += ["HTML"]

lector_Viktor = Lecturer("Виктор", "Пушилин")
lector_Viktor.courses_attached += ["Python"]
lector_Viktor.courses_attached += ["C++"]

lector_Ksenia = Lecturer("Ксения", "Шахиризадовна")
lector_Ksenia.courses_attached += ["Python"]

reviewer_Pushkin = Reviewer("Александр", "Пушкин")
reviewer_Pushkin.courses_attached += ["Python"]
reviewer_Pushkin.rate_student(student_Yura, "Python", 9)
reviewer_Pushkin.rate_student(student_Masha, "Python", 9)

reviewer_Gomer = Reviewer("Гомер", "Симпсон")
reviewer_Gomer.courses_attached += ["Python"]
reviewer_Gomer.rate_student(student_Yura, "Python", 10)
reviewer_Gomer.rate_student(student_Masha, "Python", 4)


student_Masha.rate_lector(lector_Ksenia, "Python", 2)
student_Masha.rate_lector(lector_Viktor, "Python", 9)
student_Yura.rate_lector(lector_Viktor, "Python", 5)
student_Yura.rate_lector(lector_Viktor, "C++", 5)


print(reviewer_Gomer)
print()

print(lector_Viktor)
print()

print(student_Yura)
print()

print(student_Masha)
print()

student_Masha > lector_Ksenia
lector_Ksenia < student_Yura
lector_Viktor < student_Masha


def average_student(cours, *students):
    count = 0
    grade = 0
    for i in students:
        for m in i.grades[cours]:
            grade += m
            count += 1
    if count == 0:
        print("Оценок нет!")
    print(f"Средняя оценка по курсу {cours} - {round(grade / count, 1)}")


def average_lector(cours, *lectors):
    count = 0
    grade = 0
    for lector in lectors:
        m = lector.grades.get(cours, 0)
        if m == 0:
            grade += 0
        else:
            grade += sum(m)
            count += len(m)
    if grade == 0:
        print("Оценок нет!")
    else:
        print(f"Средняя оценка по курсу {cours} - {round(grade / count, 1)}")


average_student("Python", student_Yura, student_Masha)
average_lector("Python", lector_Ksenia, lector_Viktor)
