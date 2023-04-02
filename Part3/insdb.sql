INSERT INTO Video(videoCode,videoLength) VALUES
(11,10),
(22,10),
(33,10),
(44,10),
(55,10);

INSERT INTO Model(modelNo,width,height,weight,depth,screenSize) VALUES
(11,10,20,22,3,25),
(22,12,12,15,4,15),
(33,15,30,12,5,24),
(44,12,32,44,10,62),
(55,13,24,10,10,12);

INSERT INTO Site(siteCode,type,address,phone) VALUES
(1,"Restaurant","5505 28th st","800-555-5555"),
(2,"Bar","3602 Slide rd. B11","800-555-5555"),
(3,"Bar","6405 Slide rd.","800-555-5555"),
(4,"Restaurant", "4001 4th st","800-555-5555"),
(5,"Restaurant","1234 Ave Q","800-555-5555");

INSERT INTO DigitalDisplay(serialNo,schedulerSystem,modelNo) VALUES
(12,"Random",11),
(23,"Smart",22),
(34,"Smart",33),
(45,"Virtue",44),
(56,"Random",55);
 
INSERT INTO Client(clientId,name,phone,address) VALUES
(13,"John Smith","800-555-5555","3708 25th St."),
(24,"John Doe","800-555-5555","4009 31st St."),
(35,"Jane Doe","800-555-5555","4009 31st St."),
(46,"Fistname Lastname","800-555-5555","2408 E FM 1729"),
(57,"DROP TABLE Client;","800-555-5555","Space");

INSERT INTO TechnicalSupport(empId,name,gender) VALUES
(123,"Happy Marcus","F"),
(229,"Lucas Frost","M"),
(365,"Basin Malory","M"),
(487,"Nigma Edwards","F"),
(501,"Destiny Mallot","M");

INSERT INTO Administrator(empId,name,gender) VALUES
(14,"Andebert Manjeet","M"),
(25,"Eula Bert","F"),
(36,"Javion Bernhard","M"),
(47,"Ella Demelza","F"),
(58,"Spencer Archibald","M");

INSERT INTO Salesman(empId,name,gender) VALUES
(15,"Cheyanne Deforrest","F"),
(26,"Odin Indy","M"),
(37,"Sly Bloxham","M"),
(48,"Kristina Arden","F"),
(59,"Marylu Diamond","F");

INSERT INTO AirtimePackage(packageId,class,startDate,lastDate,frequency,videoCode) VALUES
(1,"economy","2020-06-15","2020-07-15",4,11),
(2,"golden hours","2020-09-20","2020-10-20",5,21),
(3,"whole day","2020-11-30","2021-01-22",3,31),
(4,"economy","2021-03-13","2021-04-15",4,41),
(5,"golden hours","2023-01-23","2023-02-19",6,51);

INSERT INTO AdmWorkHours(empId,day,hours) VALUES
(14,"2020-06-15",08.12),
(25,"2020-06-15",07.53),
(36,"2020-06-15",05.75),
(47,"2020-06-15",08.34),
(58,"2020-06-15",07.94);

INSERT INTO Broadcasts(videoCode,siteCode) VALUES
(11,1),
(22,2),
(33,3),
(44,4),
(55,5);

INSERT INTO Administers(empId,siteCode) VALUES
(14,1),
(25,2),
(36,3),
(47,4),
(58,5);

INSERT INTO Specializes(empId,modelNo) VALUES
(123,11),
(229,22),
(365,33),
(487,44),
(501,55);

INSERT INTO Purchases(clientId,empId,packageId,commisionRate) VALUES
(13,15,1,12.55),
(24,26,2,10.33),
(35,37,3,19.99),
(46,48,4,15.01),
(57,59,5,14.44);

INSERT INTO Locates(serialNo,sitecode) VALUES
(12,1),
(23,2),
(34,3),
(45,4),
(56,5);
