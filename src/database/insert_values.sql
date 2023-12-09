
INSERT INTO Tutor (TutorID, email, name, cost, subject, location) 
VALUES (4, "antrizzo@iit.com", "Ant Rizzo", 80.00, "computer science", "online"),
(5, "pkane5@iit.com", "Patrick Kane", 10.00, "computer science", "online"),
(6, "jtoews6@iit.com", "Jonathon Toews", 15.00, "math", "online"),
(7, "burlacher7@iit.com", "Brian Urlacher", 50.00, "computer science", "online"),
(8, "mtrubisky8@iit.com", "Mitch Trubisky", 30.00, "computer science", "offline"),
(9, "btupo9@iit.com", "Bob Tupo", 100.00, "math", "offline"),
(10, "dkeith10@iit.com", "Duncan Keith", 5.00, "computer science", "offline"),
(11, "dswanson@iit.com", "Dansby Swanson", 80.00, "computer science", "online");

INSERT INTO availability (TutorID, day, timeof, filled)
VALUES(5, "monday", 11, 0),
(7, "tuesday", 11, 0),
(5, "monday", 12, 0),
(10, "friday", 9, 0),
(11, "monday", 12, 0),
(8, "friday", 4, 0),
(6, "wednesday", 1, 0),
(9, "monday", 12, 0)

INSERT INTO student (StudentID, name, email, budget, schoolYear, location)
VALUES (5, "Bob Latte", "blatte5@iitstudents.com", 40.00, 1, "online"),
(6, "Ethan Henry", "ehenry6@iitstudents.com", 35.00, 2, "online"),
(7, "Ethan Jenssen", "ejenssen7@iitstudents.com", 120.00, 3, "online"),
(8, "Mike Towers", "mtowers8@iitstudents.com", 80.00, 4, "online"),
(9, "Bad Bunny", "bbunny9@iitstudents.com", 20.00, 4, "offline"),
(10, "Joe Smith", "jsmith10@iitstudents.com", 10.00, 1, "online"),
(11, "Nico H", "nh11@iitstudents.com", 50.00, 2, "offline"),
(12, "Jesus Chavez", "jchaves12@iitstudents.com", 200.00, 1, "offline")
