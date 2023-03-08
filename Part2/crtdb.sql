CREATE TABLE Video(
    videoCode INT PRIMARY KEY,
    videoLength INT
);

CREATE TABLE Model(
    modelNo char(10) PRIMARY KEY,
    width numeric(6,2),
    screenSize numeric(6,2)
);

CREATE TABLE Site(
    siteCode integer PRIMARY KEY,
    type varchar(16),
    address varchar(100),
    phone varchar(16)
);

CREATE TABLE DigitalDisplay (
    serialNo        CHAR (10) PRIMARY KEY,
    schedulerSystem CHAR (10),
    modelNo         CHAR (10) REFERENCES Model (modelNo) 
);

CREATE TABLE Client(
    clientId INT PRIMARY KEY,
    name varchar(40),
    phone varchar(16),
    address varchar(100)
);
CREATE TABLE TechnicalSupport(
    empId  INT,
    name   VARCHAR (40),
    gender CHAR (1),
    PRIMARY KEY (empId)
);
CREATE TABLE Administrator(
    empId  INT,
    name   VARCHAR (40),
    gender CHAR (1),
    PRIMARY KEY (empId)
);
CREATE TABLE Salesman(
    empId  INT,
    name   VARCHAR (40),
    gender CHAR (1),
    PRIMARY KEY (empId)
);
CREATE TABLE AirtimePackage(
    packageId INT,
    class     VARCHAR (16),
    startDate DATE,
    lastDate  DATE,
    frequency INT,
    videoCode INT,
    PRIMARY KEY (packageId)
);
CREATE TABLE AdmWorkHours(
    empId     INT,
    day       DATE,
    hours     NUMERIC (4, 2),
    PRIMARY KEY (empId, day),
    foreign key (empId) references Administrator (empId)
);
CREATE TABLE Broadcasts(
	videoCode INT,
	siteCode INT,
	FOREIGN KEY (videoCode) references Video (videoCode),
	FOREIGN KEY (siteCode) references Site (siteCode),
	PRIMARY KEY (videoCode,siteCode)
);
CREATE TABLE Administers(
	empId INT,
	siteCode INT,
	FOREIGN KEY (empId) references Administrator (empId),
	FOREIGN KEY (siteCode) references Site (siteCode),
	PRIMARY KEY (empId,siteCode)
);
CREATE TABLE Specializes(
	empId INT,
	modelNo CHAR(10),
	FOREIGN KEY (empId) references TechnicalSupport (empId),
	FOREIGN KEY (modelNo) references Model (modelNo),
	PRIMARY KEY (empId,modelNo)
);
CREATE TABLE Purchases(
	clientId INT,
	empId INT,
	packageId INT,
	commisionRate numeric (4,2),
	FOREIGN KEY (empId) references Salesman (empId),
	FOREIGN KEY (packageId) references AirtimePackage (packageId),
	PRIMARY KEY(clientId,empId,packageId)
);
CREATE TABLE Locates(
	serialNo CHAR (10),
	siteCode INT,
	FOREIGN KEY (serialNo) references DigitalDisplay (serialNo),
	FOREIGN KEY (siteCode) references Site (siteCode),
	PRIMARY KEY (serialNo,siteCode)
);
