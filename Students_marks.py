class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.marks = {}

    def add_subject(self, subject, mark, max_mark):
        self.marks[subject] = (mark, max_mark)

    def totalObtained(self):
        return sum(mark for mark, _ in self.marks.values())

    def totalMarks(self):
        return sum(max_mark for _, max_mark in self.marks.values())

    def percentage(self):
        total_obtained = self.totalObtained()
        total_possible = self.totalMarks()
        return (total_obtained / total_possible) * 100 if total_possible > 0 else 0


def main():
    student = Student("Bob", "Happy")
    student.add_subject("Math", 90, 100)
    student.add_subject("Physics", 85, 100)
    student.add_subject("English", 95, 100)

    print(f"Total Obtained Marks: {student.totalObtained()}")
    print(f"Total Possible Marks: {student.totalMarks()}")
    print(f"Percentage: {student.percentage():.2f}%")


if __name__ == "__main__":
    main()
