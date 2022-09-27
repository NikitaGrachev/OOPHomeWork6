class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecture, course, grade):
        if isinstance(lecture, Lecture) and course in self.courses_in_progress:
            if course in lecture.grades:
                lecture.grades[course] += [grade]
            else:
                lecture.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_value_student(self):
        if not self.grades:
            return 0
        grades_list = []
        for grade in self.grades.values():
            grades_list.extend(grade)
        return sum(grades_list) / len(grades_list)

    def __str__(self):
        return f'''Имя: {self.name}
              \rФамилия: {self.surname}
              \rСредняя оценка за домашние задания: {self.average_value_student()}
              \rКурсы в процессе изучения: {', '.join(self.courses_in_progress)}
              \rЗавершенные курсы: {', '.join(self.finished_courses)}'''
    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Нельзя сравнивать разные классы!'
        return self.average_value_student() < other.average_value_student()

    def __le__(self, other):
        if not isinstance(other, Student):
            return 'Нельзя сравнивать разные классы!'
        return self.average_value_student() <= other.average_value_student()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return 'Нельзя сравнивать разные классы!'
        return self.average_value_student() == other.average_value_student()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecture(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_value(self):
        if not self.grades:
            return 0
        grades_list = []
        for grade in self.grades.values():
            grades_list.extend(grade)
        return sum(grades_list) / len(grades_list)

    def __str__(self):
        return f'''Имя: {self.name}
              \rФамилия: {self.surname}
              \rСредняя оценка за лекции: {self.average_value()}'''

    def __lt__(self, other):
        if not isinstance(other, Lecture):
            return 'Нельзя сравнивать разные классы!'
        return self.average_value() < other.average_value()

    def __le__(self, other):
        if not isinstance(other, Lecture):
            return 'Нельзя сравнивать разные классы!'
        return self.average_value() <= other.average_value()

    def __eq__(self, other):
        if not isinstance(other, Lecture):
            return 'Нельзя сравнивать разные классы!'
        return self.average_value() == other.average_value()

class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return f'''Имя: {self.name}
              \rФамилия: {self.surname}'''

def average_value_homework_allstudent(persons, course):
    if not isinstance(persons, list):
        return "Not list"
    grades_list = []
    for person in persons:
        grades_list.extend(person.grades.get(course, []))
    if not grades_list:
        return "По такому курсу ни у кого нет оценок"
    return round(sum(grades_list) / len(grades_list), 2)


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Git']

best_student.grades['Git'] = [10, 10, 10, 10, 10]
best_student.grades['Python'] = [10, 10]

best_student1 = Student('Ruo', 'Ema', 'my_gender')

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

all_student = Student('Ruoy', 'Eman', 'your_gender')
all_student.courses_in_progress += ['Python']

cool_lecture = Lecture('Some', 'Buddy')
cool_lecture.courses_attached += ['Python']
cool_lecture.courses_attached += ['Git']

cool_lecture1 = Lecture('Some', 'Buddy')

all_student.rate_hw(cool_lecture, 'Python', 10)
all_student.rate_hw(cool_lecture, 'Python', 10)
all_student.rate_hw(cool_lecture, 'Python', 10)

print(', '.join(best_student.finished_courses))
print(', '.join(best_student.courses_in_progress))
print(best_student.grades)
print(cool_lecture.grades)
print(cool_reviewer)
print(cool_lecture)
print(best_student)
print(best_student1 < best_student)
print(best_student1 <= best_student)
print(best_student1 == best_student)
print(cool_lecture1 < cool_lecture)
print(cool_lecture1 <= cool_lecture)
print(cool_lecture1 == cool_lecture)
student_list = [best_student, best_student1]
lecture_list = [cool_lecture, cool_lecture1]
print(average_value_homework_allstudent(student_list, 'Python'))
print(average_value_homework_allstudent(lecture_list, 'Python'))
