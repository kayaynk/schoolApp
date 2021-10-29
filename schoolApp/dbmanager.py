import mysql.connector as mysql
from datetime import datetime
from _connection import connection
from Student import Student
from Teacher import Teacher
from Class import Class
from Branch import Branch


class DbManager:
    def __init__(self):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def getClasses(self):
        sql = "select * from class"
        self.cursor.execute(sql)
        try:
            obj = self.cursor.fetchall()
            return Class.CreateClass(obj)
        except mysql.Error as err:
            print("Error: ", err)
    def getBranchs(self):
        sql = "select * from branch"
        self.cursor.execute(sql)
        try:
            obj = self.cursor.fetchall()
            return Branch.CreateBranch(obj)
        except mysql.Error as err:
            print("Error: ", err)

    def getStudentById(self, id):
        sql = "select * from student where id = %s"
        value = (id,)
        self.cursor.execute(sql, value)
        try:
            obj = self.cursor.fetchone()
            return Student.CreateStudent(obj)
        except mysql.Error as err:
            print("Error: ", err)

    def getStudentsByClassId(self, classid):
        sql = "select * from student where classid = %s"
        value = (classid,)
        self.cursor.execute(sql, value)
        try:
            obj = self.cursor.fetchall()
            return Student.CreateStudent(obj)


        except mysql.Error as err:
            print("Error: ", err)

    def addStudent(self, student: Student):
        sql = "INSERT INTO Student(studentNumber,name,surname,gender,birthdate,classid) VALUES (%s,%s,%s,%s,%s,%s)"
        value = (
            student.studentNumber, student.name, student.surname, student.gender, student.birthdate, student.classid)
        self.cursor.execute(sql, value)
        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayıt eklendi")
        except mysql.Error as err:
            print("Error: ", err)

    def editStudent(self, student: Student):
        sql = "Update student set studentnumber = %s, name = %s, surname= %s ,gender =%s, birthdate=%s,classid=%s where id = %s"
        value = (
            student.studentNumber, student.name, student.surname, student.gender, student.birthdate, student.classid,
            student.id)
        self.cursor.execute(sql, value)
        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayıt güncellendi")
        except mysql.Error as err:
            print("Error: ", err)
    def deleteStudent(self,studentid):
        sql = "delete from student where id=%s"
        value = (studentid,)
        self.cursor.execute(sql, value)
        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayıt silindi")
        except mysql.Error as err:
            print("Error: ", err)
    def getTeacherById(self, id):
        sql = "select * from teacher where id = %s"
        value = (id,)
        self.cursor.execute(sql, value)
        try:
            obj = self.cursor.fetchone()
            return Teacher.CreateTeacher(obj)
        except mysql.Error as err:
            print("Error: ", err)

    def getTeacherByBranchId(self, branchid):
        sql = "select * from teacher where branchid = %s"
        value = (branchid,)
        self.cursor.execute(sql, value)
        try:
            obj = self.cursor.fetchall()
            return Teacher.CreateTeacher(obj)
        except mysql.Error as err:
            print("Error: ", err)

    def addTeacher(self, teacher: Teacher):
        sql = "INSERT INTO teacher(name,surname,birthdate,gender,branchid) VALUES (%s,%s,%s,%s,%s)"
        value = (teacher.name, teacher.surname, teacher.birthdate, teacher.gender, teacher.branchid)
        self.cursor.execute(sql, value)
        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayıt eklendi")
        except mysql.Error as err:
            print("Error: ", err)

    def editTeacher(self, teacher: Teacher):
        sql = "update teacher set branch= %s, name = %s, surname = %s,birthdate = %s, gender=%s where id=%s"
        value = (teacher.name, teacher.surname, teacher.birthdate, teacher.gender, teacher.id, teacher.branchid)
        self.cursor.execute(sql, value)
        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayıt eklendi")
        except mysql.Error as err:
            print("Error: ", err)
    # def __del__(self):
    #     self.connection.close()
    #     print("Database is closed")

# # db=DbManager()
# # student = db.getStudentById(7)
# # student[0].name="Hasan Kaya"
# # student[0].surname="Yanıkomeroglu"
# # student[0].studentNumber="8240"
# # student[0].gender="E"
# # db.editStudent(student[0])
# # student = db.getStudentsByClassId(1)
# # print(student[4].name)
# # # print(student[0].surname)
# # # print(student[0].studentNumber)
# db = DbManager()
# teacher = db.getTeacherByBranchId(4)
# # teacher[0].name="Hasan Kaya"
# # teacher[0].surname="Yanıkomeroglu"
# # teacher[0].
# # teacher[0].gender="E"
# print(teacher[0].name)
