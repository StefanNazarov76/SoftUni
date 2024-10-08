class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name: str, grade: float):
        if len(self.students) < Class.__students_count:
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        average_grade = sum(self.grades) / len(self.grades)
        return round(average_grade, 2)

    def __repr__(self):
        students = ', '.join(self.students)
        average_grade = self.get_average_grade()
        return f'The students in {self.name}: {students}. Average grade: {average_grade}'

