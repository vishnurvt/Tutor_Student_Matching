import mysql.connector 

#connecting to mysql database
mydb = mysql.connector.connect (
    host = "localhost",
    user = "root",
    passwd = "0000",
    database = "teacher_student_matching"
)

#creating a cursor for the database
mycursor = mydb.cursor()


#opening statements to being application 
print("Hello, welcome to our tutor-student matching application!")
print("If you are a student, please type S into the console")
print("If you are a tutor, please type T into the console")

input1 = input()

#allows tutor to register. takes in input data, stores as variables, then assigns those variables to the sql INSERT INTO statement
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

#same as tutorRegister, allows student to register. takes in input data, stores as variables, then assigns those variables to the sql INSERT INTO statement
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

#allows tutor to add timeslots. takes in day and time as inputs and tutorid as argument to be able to insert the correct information with the sql statement
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

#allows student to view all tutors that matches their subject, cost, and online/offline needs
#Only selects tutors in which are not filled (FILLED = 0)
def viewTutors(id):
    print("Type the subject you need tutoring for")
    subject = input()
    
    sql = "SELECT budget FROM student WHERE studentid = %s"
    val = (id,)
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    for x in myresult:
        budget = x[0]
        
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

#Allows student to sign up for tutor time slot. takes in input data about the tutor and time slot to correctly insert into the tutor-student matching relation
#also updates availability of the tutor to be set as FILLED
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


#allows tutors to view all students they teach. takes in tutorid as argument to query the specific tutor from the database
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


#Allows tutors to see SUM of all income from their students. uses a SELECT query sql statement 
def studentSales(id):
    sql = "SELECT SUM(cost) FROM tutor INNER JOIN tutorstudent ON tutor.tutorID = tutorstudent.tutorID WHERE tutor.tutorID = %s"
    val = (id,)
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    for x in myresult:
        print("Your total weekly income is") 
        print(str(x[0])+ " dollars per week!")


#allows students to edit their profile. uses an UPDATE sql command to update the tuple of the particular student
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

if input1 == "T": # Tutor side 
    print ("Welcome Tutor!")
    print("If you are an existing tutor, type T into the console. Or if you would like to register as a tutor, please type R")
    input1 = input()
    if input1 == "R":
        tutorRegister()#calls tutor register function to register a tutor
        print("congrats! you are now registered")
    print("Welcome Tutor!")
    print("type in your tutor id!")
    id = input()
    print("If you would like to add time slots to your schedule, please type ADD")
    print("If you would like to view your students that you tutor, type VIEW")
    input1= input()
    if input1 == "ADD":
        teacherADD(id) #calls teacherass function to add a timeslot for the tutor
        print("Time slot added!")
    else:
        viewStudents(id) #calls view students for tutors to view all of their students
        print("Type SALES to see your weekly income from tutoring all of your students")
        if input() == "SALES":
            studentSales(id) #calls sales to see sum of all income from students 


elif input1 == 'S': #Student side 
    print ("Welcome Student!")
    print("If you have already registered, type S into the console. Or if you would like to register, please type R")
    input1 = input()
    if input1 == "R":
        StudentRegister() #calls student register function to carry out tasks
        print("congrats! you are now registered")
    print("Welcome Student!")
    print("Type in your student ID!")
    id = input()
    print("If you would like to see available tutors for you desires, please type VIEW")
    print("If you would like to change your budget, preffered location, or year, type EDIT")
    if input() == "VIEW": 
        viewTutors(id) #Calls viewtutors function to view available tutors
        print("if you would like to sign up for one of these tutors, type ADD. To exit, type 0")
        input2 = input()
        if input2 == 0:
            exit()
        if input2 == "ADD":
            addtutor(id) #calls add tutor function to add all tutors 
            print("congrats! you have signed up for this tutor!")
    else:
        edit(id) #calls edit function for student to edit their profile
