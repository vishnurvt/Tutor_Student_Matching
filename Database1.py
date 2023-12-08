import mysql.connector 

mydb = mysql.connector.connect (
    host = "localhost",
    user = "root",
    passwd = "0000",
    database = "teacher_student_matching"
)

mycursor = mydb.cursor()

print("Hello, welcome to our tutor-student matching application!")
print("If you are a student, please type S into the console")
print("If you are a tutor, please type T into the console")

input1 = input()

def tutorRegister():
    print("We are glad you would like to register!")
    print("Please type in your teaching ID")
    t_id = input()
    print("Please type in your name")
    name = input()
    print("Please type in your email")
    email = input()
    print("Please type in your hourly cost")
    cost = input()
    print("Please type in whether you are an online tutor or an offline tutor (Type online or offline)")
    location = input()
    print("Please type in the subject you are capable of tutoring for")
    subject = input()

    sql = "INSERT INTO Tutor (TutorID, email, name, cost, subject, location) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (t_id, email, name, cost, subject, location)
    mycursor.execute(sql,val)
    mydb.commit()
    return 

def StudentRegister():
    print("To register, fill out all prompts")
    print("please type in you student id to register")
    id = int(input())
   
    print("type in your name")
    name = input()

    print("type in your email")
    email = input()
    print("type in your budget")
    budget = int(input())
    print("type in your year in school")
    yr = int(input())
    print("Type in your preference of offline or online")
    o = input()

    sql = "INSERT INTO student (StudentId, name, email, budget, SchoolYear, location) VALUES (%s, %s,%s, %s,%s, %s)"
    val = (id, name, email,budget, yr, o)
    mycursor.execute(sql, val)
    mydb.commit()
    return

def teacherADD(id):
    print("Please type in the day of the week you would like to tutor")
    day = input()
    print("Please put in the time that you can tutor on that day")
    t = input()
    sql = "INSERT INTO availability (TutorID, day, timeof, filled) VALUES(%s, %s, %s, %s)"
    val = (id, day, t, 0)
    mycursor.execute(sql, val)
    mydb.commit()
    return

def viewTutors(id):
    print("Type the subject you need tutoring for")
    subject = input()
    # print("Type whether you want an online tutor or offline")
    # location = input()
    sql = "SELECT budget FROM student WHERE studentid = %s"
    val = (id,)
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    for x in myresult:
        budget = x[0]
        print("budget ISSSS " + str(budget))
    sql = "SELECT location FROM student WHERE studentid = %s"
    val = (id,)
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    for x in myresult:
        location = x[0]

    sql = "SELECT tutor.tutorid, tutor.name AS TutorName, tutor.email AS TutorEmail, tutor.cost AS TutorCost, availability.day as Day, availability.timeof as Time FROM tutor INNER JOIN availability ON tutor.TutorID = availability.TutorID WHERE tutor.cost <= %s and tutor.subject = \"" + subject + "\"" + "and tutor.location = \"" + location + "\" and availability.filled = 0"
    val = (budget,)

    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    i = 1
    for x in myresult:
        print("teacher: " + str(i)) 
        print(x)
        i+=1
    print("You have " + str(i-1) + " teachers to choose from")
    return 

def addtutor(id):
    print("Please type in the id of the tutor you would like to sign up for")
    tid = input()
    print("Please type the day they are available")
    d = input()
    print("Please type the time they are available")
    t = input()
    print("Please type in the subject")
    sub = input()
    sql = "INSERT INTO TutorStudent (TutorID, StudentID, subject, day, timeof) VALUES(%s, %s, %s, %s, %s)"
    val = (tid, id, sub, d, t)
    mycursor.execute(sql, val)
    mydb.commit()
    sql = "UPDATE availability SET filled = 1 WHERE Tutorid = %s and day = \"" + d + "\" and timeof = %s"
    val = (tid,t)
    mycursor.execute(sql,val)
    mydb.commit()
    return

def viewStudents(id):
    sql = "SELECT * FROM tutorstudent WHERE tutorID = %s"
    val = (id,)
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    i = 1
    for x in myresult:
        print("Student: " + str(i)) 
        print(x)
        i+=1
    print("You have " + str(i-1) + " total students")
    return
def studentSales(id):
    sql = "SELECT SUM(cost) FROM tutor INNER JOIN tutorstudent ON tutor.tutorID = tutorstudent.tutorID WHERE tutor.tutorID = %s"
    val = (id,)
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    for x in myresult:
        print("Your total weekly income is") 
        print(str(x[0])+ " dollars per week!")


def edit(id):
    print("Type what you would like to edit in your profile (budget, location, or year)")
    att = input()
    print("What would you like to change it to?")
    new = input()
    if att == "location":
        n = "\"" + new + "\""
    else:
        n = new
    sql = "UPDATE student SET " + att +  " = " + n + " WHERE studentID = " + id 
    mycursor.execute(sql)
    mydb.commit()
    print("Your profile has been edited!")
    return
#main code 

if input1 == "T":
    print ("Welcome Tutor!")
    print("If you are an existing tutor, type T into the console. Or if you would like to register as a tutor, please type R")
    input1 = input()
    if input1 == "R":
        tutorRegister()
        print("congrats! you are now registered")
    print("Welcome Tutor!")
    print("type in your tutor id!")
    id = input()
    print("If you would like to add time slots to your schedule, please type ADD")
    print("If you would like to view your students that you tutor, type VIEW")
    input1= input()
    if input1 == "ADD":
        teacherADD(id)
        print("Time slot added!")
    else:
        viewStudents(id)
        print("Type SALES to see your weekly income from tutoring all of your students")
        if input() == "SALES":
            studentSales(id)


elif input1 == 'S':
    print ("Welcome Student!")
    print("If you have already registered, type S into the console. Or if you would like to register, please type R")
    input1 = input()
    if input1 == "R":
        StudentRegister()
        print("congrats! you are now registered")
    print("Welcome Student!")
    print("Type in your student ID!")
    id = input()
    print("If you would like to see available tutors for you desires, please type VIEW")
    print("If you would like to change your budget, preffered location, or year, type EDIT")
    if input() == "VIEW":
        viewTutors(id)
        print("if you would like to sign up for one of these tutors, type ADD. To exit, type 0")
        input2 = input()
        if input2 == 0:
            exit()
        if input2 == "ADD":
            addtutor(id)
            print("congrats! you have signed up for this tutor!")
    else:
        edit(id)



        
    