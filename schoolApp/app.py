import datetime

from Student import Student
from Teacher import Teacher
from dbmanager import DbManager


class App:
    def __init__(self):
        self.db = DbManager()

    def initApp(self):
        msg = "****\n1-Student List\n2-Add Student\n3-Update Student\n4-Delete Student\n5-Add Teacher\n6-Teacher List\n7-Listing By Classes\n8-Exit(Press E or Q)"
        while True:
            print(msg)
            process = input("Vote: ")
            if process == "1":
                self.displayStudents()
            elif process == "2":
                self.addStudents()
            elif process == "3":
                self.editStudent()
            elif process == "4":
                self.deleteStudent()
            elif process == "5":
                self.addTeacher()
            elif process == "6":
                self.displayTeachers()
            elif process == "7":
                self.displayClasses()
            elif process == "E" or process == "e" or process == "Q" or process == "q":
                break
            else:
                print("Incorrect entry")

    def addStudents(self):
        self.displayClasses()
        classid = int(input("Which Class: "))
        number = input("Student Number: ")
        name = input("Name: ")
        surname = input("Surname: ")
        year = int(input("Year: "))
        month = int(input("Month: "))
        day = int(input("Day: "))
        birthdate = datetime.date(year, month, day)
        gender = input("Gender: ")
        student = Student(None, number, name, surname, gender, birthdate, classid)
        self.db.addStudent(student)

    def editStudent(self):
        classid = self.displayStudents()
        studentid = int(input("Student Id: "))
        student = self.db.getStudentById(studentid)
        student[0].name = input("Name: ") or student[0].name
        student[0].surname = input("Surname: ") or student[0].surname
        student[0].gender = input("Gender(E/K): ") or student[0].gender
        student[0].classid = input("Class:") or student[0].classid
        year = input("Year: ") or student[0].birthdate.year
        month = input("Month: ") or student[0].birthdate.month
        day = input("Day: ") or student[0].birthdate.day
        student[0].birthdate = datetime.date(year, month, day)
        self.db.editStudent(student[0])

    def deleteStudent(self):
        classid = self.displayStudents()
        studentid = int(input("Student Id: "))

        self.db.deleteStudent(studentid)

    def displayClasses(self):
        classes = self.db.getClasses()
        for c in classes:
            print(f"{c.id}: {c.name}")

    def displayStudents(self):
        self.displayClasses()
        classid = input("Which Class: ")

        students = self.db.getStudentsByClassId(classid)
        print("Student List")
        for std in students:
            print(f"{std.id}-{std.studentNumber} {std.name} {std.surname}")
        return classid
    def displayTeachers(self):
        self.displayBranch()
        branchid = input("Which Branch: ")
        teachers = self.db.getTeacherByBranchId(branchid)
        print("Teacher List")
        for teach in teachers:
            print(f"{teach.id}--{teach.name} {teach.surname}")
    def addTeacher(self):
        self.displayBranch()
        branchid = int(input("Which Branch: "))
        name = input("Name: ")
        surname = input("Surname: ")
        year = int(input("Year: "))
        month = int(input("Month: "))
        day = int(input("Day: "))
        birthdate = datetime.date(year, month, day)
        gender = input("Gender: ")
        teacher = Teacher(None, name, surname,birthdate,gender, branchid)
        self.db.addTeacher(teacher)

    def displayBranch(self):
        branchs = self.db.getBranchs()
        for b in branchs:
            print(f"{b.id}: {b.name}")


app = App()
app.initApp()
