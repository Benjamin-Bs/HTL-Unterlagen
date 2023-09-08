-- MariaDB dump 10.19  Distrib 10.5.10-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: bibliothek
-- ------------------------------------------------------
-- Server version	10.5.10-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `t_buecher`
--

DROP TABLE IF EXISTS `t_buecher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_buecher` (
  `isbn` varchar(13) NOT NULL DEFAULT '',
  `titel` varchar(100) DEFAULT NULL,
  `autor` varchar(100) DEFAULT NULL,
  `auflage` int(11) DEFAULT NULL,
  `preis` float DEFAULT NULL,
  PRIMARY KEY (`isbn`),
  KEY `i_autor` (`autor`),
  KEY `i_titel` (`titel`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_buecher`
--

LOCK TABLES `t_buecher` WRITE;
/*!40000 ALTER TABLE `t_buecher` DISABLE KEYS */;
INSERT INTO `t_buecher` VALUES ('1-234-56789-0','Der Baum','Gerd Baumann',1,29.95),('1-254-56649-0','Mein Gartenbuch','Bernd Blume',2,19.95),('1-285-54709-0','Fit for Fun','Brigitte Schoene',3,21.55);
/*!40000 ALTER TABLE `t_buecher` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_leser`
--

DROP TABLE IF EXISTS `t_leser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_leser` (
  `nr` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  `vname` varchar(30) DEFAULT NULL,
  `plz` varchar(5) DEFAULT NULL,
  `ort` varchar(100) DEFAULT NULL,
  `str` varchar(100) DEFAULT NULL,
  `hnr` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`nr`),
  KEY `i_leser_ab` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_leser`
--

LOCK TABLES `t_leser` WRITE;
/*!40000 ALTER TABLE `t_leser` DISABLE KEYS */;
INSERT INTO `t_leser` VALUES (1,'Husler','Bernd','10115','Berlin','Waldweg','4'),(2,'Kramer','Birgit','10119','Hainig','Steinstr.','44');
/*!40000 ALTER TABLE `t_leser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_mess`
--

DROP TABLE IF EXISTS `t_mess`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_mess` (
  `nr` int(11) NOT NULL AUTO_INCREMENT,
  `wert` int(11) DEFAULT NULL,
  PRIMARY KEY (`nr`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_mess`
--

LOCK TABLES `t_mess` WRITE;
/*!40000 ALTER TABLE `t_mess` DISABLE KEYS */;
INSERT INTO `t_mess` VALUES (1,617),(2,852),(3,406),(4,474),(5,151),(6,333),(7,211),(8,57),(9,647),(10,67),(11,389),(12,746);
/*!40000 ALTER TABLE `t_mess` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_verleih`
--

DROP TABLE IF EXISTS `t_verleih`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_verleih` (
  `isbn` varchar(13) NOT NULL DEFAULT '',
  `leser` int(11) NOT NULL DEFAULT 0,
  `datum` date DEFAULT NULL,
  KEY `i_ausleihe` (`isbn`,`leser`),
  KEY `i_verleih` (`isbn`,`leser`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_verleih`
--

LOCK TABLES `t_verleih` WRITE;
/*!40000 ALTER TABLE `t_verleih` DISABLE KEYS */;
INSERT INTO `t_verleih` VALUES ('1-254-56649-0',1,'2021-05-27'),('1-234-56789-0',1,'2021-04-01'),('1-285-54709-0',2,'2021-04-25'),('1-285-54709-0',3,'2018-01-24');
/*!40000 ALTER TABLE `t_verleih` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-02 16:22:38
