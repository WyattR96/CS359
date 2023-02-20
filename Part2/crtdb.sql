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