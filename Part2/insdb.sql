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

INSERT INTO TechnicalSupport(empId,name,gender) VALUES
(123,"Happy Marcus","F"),
(229,"Lucas Frost","M"),
(365,"Basin Malory","M"),
(487,"Nigma Edwards","F"),
(501,"Destiny Mallot","M");

INSERT INTO Administrator(empId,name,gender) VALUES
(1,"Andebert Manjeet","M"),
(2,"Eula Bert","F"),
(3,"Javion Bernhard","M"),
(4,"Ella Demelza","F"),
(5,"Spencer Archibald","M");

INSERT INTO Salesman(empId,name,gender) VALUES
(1,"Cheyanne Deforrest","F"),
(2,"Odin Indy","M"),
(3,"Sly Bloxham","M"),
(4,"Kristina Arden","F"),
(5,"Marylu Diamond","F");

INSERT INTO AirtimePackage(packageId,class,startDate,lastDate,frequency,videoCode) VALUES
(1,"economy","2020-06-15","2020-07-15",4,11),
(2,"golden hours","2020-09-20","2020-10-20",5,21),
(3,"whole day","2020-11-30","2021-01-22",3,31),
(4,"economy","2021-03-13","2021-04-15",4,41),
(5,"golden hours","2023-01-23","2023-02-19",6,51);

INSERT INTO AdmWorkHours(empId,day,hours) VALUES
(1,"2020-06-15",08.12),
(2,"2020-06-15",07.53),
(3,"2020-06-15",05.75),
(4,"2020-06-15",08.34),
(5,"2020-06-15",07.94);

INSERT INTO Broadcasts(videoCode,siteCode) VALUES
(1,1),
(2,2),
(3,3),
(4,4),
(5,5);

INSERT INTO Administers(empId,siteCode) VALUES
(1,1),
(2,2),
(3,3),
(4,4),
(5,5);

INSERT INTO Specializes(empId,modelNo) VALUES
(1,1),
(2,2),
(3,3),
(4,4),
(5,5);

INSERT INTO Purchases(clientId,empId,packageId,commisionRate) VALUES
(1,1,1,12.55),
(2,2,2,10.33),
(3,3,3,19.99),
(4,4,4,15.01),
(5,5,5,14.44);

INSERT INTO Locates(serialNo,sitecode) VALUES
(1,1),
(2,2),
(3,3),
(4,4),
(5,5);
