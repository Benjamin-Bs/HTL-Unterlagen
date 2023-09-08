drop TABLE TabelleA;
CREATE TABLE TabelleA(
	ID INTEGER,
	Name VARCHAR(20),
	Vorname VARCHAR(20),
	Nr INTEGER
	);
INSERT INTO TabelleA VALUES (1,'Naumann','Steve',1);
INSERT INTO TabelleA VALUES (2,'Baumann','Janine',1);
INSERT INTO TabelleA VALUES (3,'Hartmann','Heike',7);
INSERT INTO TabelleA VALUES (4,'Naumann','Jens',11);

DROP TABLE TabelleB;
CREATE TABLE TabelleB(
	Nr INTEGER,
	Abteilung VARCHAR(20)
	);
	INSERT INTO TabelleB VALUES (1,'Einkauf');
	INSERT INTO TabelleB VALUES (7,'Personal');
	INSERT INTO TabelleB VALUES (10,'EDV');
	