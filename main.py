import pymysql 

mydb = pymysql.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="school"
)

query= "CREATE DATABASE IF NOT EXISTS school"
cursor = mydb.cursor()

cursor.execute(query)

#create database
def create_table():
    query = """
                CREATE TABLE IF NOT EXISTS students(
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    name  VARCHAR(50) NOT NULL,
                    age INT,
                    grade FLOAT
                )
            """
    cursor = mydb.cursor()
    cursor.execute(query)

 #insert into table   
def add_student(name, age, grade):
    query = """
            INSERT INTO students(name, age, grade)
            values(%s, %s, %s)
        """
    cursor = mydb.cursor()
    cursor.execute(query, (name, age, grade))

    mydb.commit()

#update table colums = grade
def update_greade(id, grade):
    query = """
                UPDATE students
                SET grade = %s
                WHERE id = %s
            """
    cursor = mydb.cursor()
    cursor.execute(query, (grade, id))

    mydb.commit()

def increase_age(id, val):
    query = "SELECT age FROM students WHERE id = %s"
    cursor = mydb.cursor()
    cursor.execute(query, (id))

    age = cursor.fetchone()
    newage = age[0] + val

    cursor.execute("""
                    UPDATE students
                    SET age = %s
                    WHERE id = %s
                    """, (newage, id)
                   )
    mydb.commit()

def view_all_students():
    query = "SELECT * from students"
    cursor = mydb.cursor()
    cursor.execute(query)
    students = cursor.fetchall()
    for student in students:
        print(f""" 
                id = {student[0]}
                name = {student[1]}
                age = {student[2]}
                grade = {student[3]}
            """)

while True:
    print(""" 
            1. Create Table
            2. Add Student
            3. Update Grade
            4. Increase Age
            5. View All Student
            0. Exit
        """)
    
    option = int(input("Enter Option: "))

    if(option == 1):
        # tablename = input("Enter Tablename: ")
        create_table()

    elif(option == 2):
        name = input("Enter Name: ")
        age = int( input("Enter Age: "))
        grade = float(input("Enter Grade: "))
        add_student(name,age,grade)

    elif(option == 3):
        id = int(input("Enter ID: "))
        grade = float(input("Enter Grade: "))
        update_greade(id, grade)
    elif(option == 4):
        id = int(input("Enter ID: "))
        val = int(input("Enter number of age u went to incress: "))
        increase_age(id, val)
    elif(option == 5):
        view_all_students()
    elif(option == 0):
        break
    else:
        print("Wrong Option Selected")
    