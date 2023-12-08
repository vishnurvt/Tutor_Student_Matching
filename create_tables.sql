SQL Create Tables code:

CREATE TABLE Availability (
    TutorID INT,
    day varchar(255),
    timeof INT, 
    filled bool,
    PRIMARY KEY (TutorID, day, timeof)
    
    
); 
CREATE TABLE Student (
    StudentID INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    Email VARCHAR(255) NOT NULL,
    Day VARCHAR(255),
    timeof INT
    Location VARCHAR(255),
    Budget DECIMAL(10, 2),
    SchoolYear INT
    
);

CREATE TABLE Tutor (
    TutorID INT PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL, 
    cost DECIMAL(10, 2),
    subject VARCHAR(255),
    location VARCHAR(255)
);

CREATE TABLE TutorStudent (
    TutorID INT,
    StudentID INT,
    subject VARCHAR(255),
    day VARCHAR(255),
    timeof INT,
	PRIMARY KEY (TutorID, StudentID, subject, day, timeof)
);





