
USE gesund;

CREATE TABLE Person
(
    PId      INT PRIMARY KEY,
    PName    VARCHAR(255),
    PAddress VARCHAR(255),
    PGeb     DATE,
    PInfo    VARCHAR(1000)
);

CREATE TABLE Kategorie
(
    KatId   INT PRIMARY KEY,
    KatName VARCHAR(255),
    KatBem  VARCHAR(1000)
);

CREATE TABLE Krankheit
(
    KId        INT PRIMARY KEY,
    KName      VARCHAR(255),
    KStufe     INT,
    KBeschr    MEDIUMTEXT,
    KKategorie INT,
    FOREIGN KEY (KKategorie) REFERENCES Kategorie (KatId)
);


CREATE TABLE Krankenstand
(
    KraId         INT PRIMARY KEY,
    KraDate       DATE,
    KraBem        MEDIUMTEXT,
    KranKrankheit INT,
    KraPerson     INT,
    FOREIGN KEY (KranKrankheit) REFERENCES Krankheit (KId),
    FOREIGN KEY (KraPerson) REFERENCES Person (PId)
);

INSERT INTO person (PId, PName, PAddress, PGeb, PInfo) VALUES (1, 'Max Mustermann', 'Musterstraße 4, Musterstadt', '1998-06-01', 'Eine Information über Max Mustermann.');
INSERT INTO person (PId, PName, PAddress, PGeb, PInfo) VALUES (2, 'Tom Tomermann', 'Musterstraße 1, Musterstadt', '1980-03-05', 'Eine Information über Tom Tomermann.');
INSERT INTO person (PId, PName, PAddress, PGeb, PInfo) VALUES (3, 'Mia Miafrau', 'Teststraße 3, Teststadt', '1990-05-01', 'Eine Information über Mia Miafrau.');
INSERT INTO person (PId, PName, PAddress, PGeb, PInfo) VALUES (4, 'Bob Boblio', 'Keinmusterstraße 1, Keinmusterstadt', '1990-12-01', 'Eine Information über Bob Boblio.');
INSERT INTO person (PId, PName, PAddress, PGeb, PInfo) VALUES (5, 'Tom Mannberg', 'Musterland 19, Musterstadt', '1994-01-01', 'Eine Information über Tom Mannberg   .');


INSERT INTO Kategorie(katid, katname, katbem) VALUES (4,'Alergie','Keine Ahnung');
INSERT INTO Kategorie(katid, katname, katbem) VALUES (5,'Diabetes','Keine Ahnung');
INSERT INTO Kategorie(katid, katname, katbem) VALUES (6,'Hypertonie','Keine Ahnung');
INSERT INTO Kategorie(katid, katname, katbem) VALUES (7,'Depression','Keine Ahnung');


INSERT INTO Krankheit (KId, KName, KStufe, Kbeschr, Kkategorie) VALUES
                                                                    (1, 'Allergie', 'Mild', 'Eine leichte allergische Reaktion mit Juckreiz und Niesen.', 4),
                                                                    (2, 'Diabetes', 'Schwer', 'Eine chronische Stoffwechselerkrankung mit erhöhtem Blutzuckerspiegel.', 5),
                                                                    (3, 'Hypertonie', 'Mittel', 'Ein mittlerer Bluthochdruck mit erhöhten systolischen und diastolischen Werten.', 6),
                                                                    (4, 'Depression', 'Schwer', 'Eine schwere psychische Erkrankung mit anhaltender Niedergeschlagenheit und Interessensverlust.', 7);


    INSERT INTO Krankenstand(KraId, KraDate, KraBem, KranKrankheit, KraPerson) VALUES (1,'1992-03-01','keine Ahnung',1,1);
    INSERT INTO Krankenstand(KraId, KraDate, KraBem, KranKrankheit, KraPerson) VALUES (2,'1989-09-04','keine Ahnung',2,2);
    INSERT INTO Krankenstand(KraId, KraDate, KraBem, KranKrankheit, KraPerson) VALUES (3,'1978-03-05','keine Ahnung',3,3);
    INSERT INTO Krankenstand(KraId, KraDate, KraBem, KranKrankheit, KraPerson) VALUES (4,'1934-11-17','Keine Ahnung',4,4);
