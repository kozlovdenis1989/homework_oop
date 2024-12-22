class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            raise PermissionError('rate_hw(). Error in block (if)')


    def average_score(self, grade = None):
        average = []
        if grade == None:
            for value in self.grades.values():
                average.append(sum(value) / len(value))
            return sum(average) / len(average)
        else:
            return sum(self.grades[grade]) / len(self.grades[grade])

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.average_score()}\n'
                f'Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {', '.join(self.finished_courses)}')

    def __eq__(self, other):
        return self.average_score() == other.average_score()

    def __le__(self, other):
        return self.average_score() <= other.average_score()
    def __lt__(self, other):
        return self.average_score() < other.average_score()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            raise PermissionError('rate_hw(). Error in block (if)')


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def rate_hw(self, student, course, grade):
        raise PermissionError('This method nis not available for this class')

    def average_score(self, grade = None):
        average = []
        if grade == None:
            for value in self.grades.values():
                average.append(sum(value) / len(value))
            return sum(average) / len(average)
        else:
            return sum(self.grades[grade]) / len(self.grades[grade])

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.average_score()}')

    def __eq__(self, other):
        return self.average_score() == other.average_score()

    def __le__(self, other):
        return self.average_score() <= other.average_score()

    def __lt__(self, other):
        return self.average_score() < other.average_score()

class Reviewer(Mentor):
    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}')


# Create students
some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python', 'Git']
some_student.finished_courses += ["Введение в программирование"]
some_student_1 = Student('Denis', 'Kozlov', 'your_gender')
some_student_1.courses_in_progress += ['Python', 'Git']
some_student_1.finished_courses += ["Введение в программирование"]

# Create reviewers
some_reviewer = Reviewer('Some_rev_1', 'Buddy_rev_1')
some_reviewer.courses_attached += ['Python', 'Git']
some_reviewer_1 = Reviewer('Some_rev_2', 'Buddy_rev_2')
some_reviewer_1.courses_attached += ['Python', 'Git']

# Create lectures
some_lecturer = Lecturer('Some_lec_1', 'Buddy_lec_1')
some_lecturer.courses_attached += ['Python', 'Git']
some_lecturer_1 = Lecturer('Some_lec_2', 'Buddy_lec_2')
some_lecturer_1.courses_attached += ['Python', 'Git']

# Setting grades for students
some_reviewer.rate_hw(some_student, 'Git', 10)
some_reviewer.rate_hw(some_student, 'Python', 6)
some_reviewer_1.rate_hw(some_student_1, 'Git', 9)
some_reviewer_1.rate_hw(some_student_1, 'Python', 10)

# Setting grades for lectures
some_student.rate_hw(some_lecturer, 'Python', 9)
some_student.rate_hw(some_lecturer, 'Git', 7)
some_student_1.rate_hw(some_lecturer_1, 'Python', 6)
some_student_1.rate_hw(some_lecturer_1, 'Git', 6)

# Date for all objects
print('Эксперты:', some_reviewer, some_reviewer_1, sep='\n', end='\n\n')
print('Лекторы:', some_lecturer, some_lecturer_1, sep='\n', end='\n\n')
print('Студенты:', some_student, some_student_1, sep='\n', end='\n\n')

# Magic methods
print(f'== {some_student == some_student_1}')
print(f'< {some_student < some_student_1}')
print(f'> {some_student > some_student_1}')
print(f'<= {some_lecturer_1 <= some_lecturer}')
print(f'>= {some_lecturer_1>= some_lecturer}')
print(f'!= {some_student != some_student_1}')
print()

# Create a function for calculating the average of all
def average_score_objects_all(list_objects: list,  course: str):
    average = []
    object_class_name = list_objects[0].__class__.__name__

    for object in list_objects:
        average.append(object.average_score(course))

    return f'Средняя оценка у {object_class_name} за курс {course}: {sum(average) / len(average)}'


# Create lists of students and lectures
students = [some_student, some_student_1]
lectures = [some_lecturer, some_lecturer_1]


print(average_score_objects_all(students, 'Python'))
print(average_score_objects_all(lectures, 'Python'))
print(average_score_objects_all(students, 'Git'))
print(average_score_objects_all(lectures, 'Git'))