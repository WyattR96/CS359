INSERT INTO Video(videoCode,videoLength) VALUES
(1,10),
(2,10),
(3,10),
(4,10),
(5,10);

INSERT INTO Model(modelNo,width,screenSize) VALUES
(1,10.25,10.25),
(2,10.25,10.25),
(3,10.25,10.25),
(4,10.25,10.25),
(5,10.25,10.25);

INSERT INTO Site(siteCode,type,address,phone) VALUES
(1,"Restaurant","5505 28th st","800-555-5555"),
(2,"Shop","3602 Slide rd. B11","800-555-5555"),
(3,"Mall","6405 Slide rd.","800-555-5555"),
(4,"Restaraunt", "4001 4th st","800-555-5555"),
(5,"Shop","1234 Ave Q","800-555-5555");

INSERT INTO DigitalDisplay(serialNo,schedulerSystem,modelNo) VALUES
(1,"Yes",1),
(2,"Yes",2),
(3,"Yes",3),
(4,"Yes",4),
(5,"Yes",5);
 
INSERT INTO Client(clientId,name,phone,address) VALUES
(1,"John Smith","800-555-5555","3708 25th St."),
(2,"John Doe","800-555-5555","4009 31st St."),
(3,"Jane Doe","800-555-5555","4009 31st St."),
(4,"Fistname Lastname","800-555-5555","2408 E FM 1729"),
(5,"DROP TABLE Client;","800-555-5555","Space");