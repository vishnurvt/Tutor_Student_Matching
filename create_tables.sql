-- Create the Student table
CREATE TABLE Student (
    StudentID INT PRIMARY KEY,
    Email VARCHAR(255) NOT NULL,
    Date DATE,
    Time TIME,
    Location VARCHAR(255),
    Budget DECIMAL(10, 2),
    DateOfBirth DATE,
    Age INT,
    SchoolYear INT
    FOREIGN KEY (Date) REFERENCES Availability(Date)
    FOREIGN KEY (Time) REFERENCES Availability(Time)
);

-- Create the Tutor table
CREATE TABLE Tutor (
    TutorID INT PRIMARY KEY,
    Email VARCHAR(255) NOT NULL,
    Location VARCHAR(255),
    Cost DECIMAL(10, 2)
    Date DATE,
    Time TIME,
    FOREIGN KEY (Date) REFERENCES Availability(Date)
    FOREIGN KEY (Time) REFERENCES Availability(Time)
);

-- Create the TutorStudent (previous matches) table
CREATE TABLE TutorStudent (
    TutorID INT,
    StudentID INT,
    Subject VARCHAR(255),
    FOREIGN KEY (TutorID) REFERENCES Tutor(TutorID),
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID)
);

-- Create the Courses table
CREATE TABLE Courses (
    CourseID INT PRIMARY KEY,
    CourseName VARCHAR(255),
    Department VARCHAR(255),
    CourseNumber INT
);

-- Create the Availability table
CREATE TABLE Availability (
    TutorID INT,
    Date DATE,
    Time TIME,
    FOREIGN KEY (TutorID) REFERENCES Tutor(TutorID)
); 
