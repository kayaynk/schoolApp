import mysql.connector as mysql
connection = mysql.connect(
    host="localhost",
    user="root",
    password="<mysql password>",
    database="schooldb"
)
