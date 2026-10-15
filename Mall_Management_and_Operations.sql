-- MySQL dump 10.13  Distrib 8.0.45, for Win64 (x86_64)
--
-- Host: localhost    Database: mall management and operations
-- ------------------------------------------------------
-- Server version	8.0.45

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `behaviour_analytics`
--

DROP TABLE IF EXISTS `behaviour_analytics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `behaviour_analytics` (
  `CUSTOMER_ID` char(6) NOT NULL,
  `GENDER` char(10) DEFAULT NULL,
  `age` char(3) DEFAULT NULL,
  `annual_income` char(10) DEFAULT NULL,
  `spending_score` char(3) DEFAULT NULL,
  `CITY` char(50) DEFAULT NULL,
  `purchase_history` char(5) DEFAULT NULL,
  `PAYMENT_METHOD` char(10) DEFAULT NULL,
  `TRAFFIC_SOURCE` char(20) DEFAULT NULL,
  `cart_abd_rate` char(5) DEFAULT NULL,
  `LOYALTY` char(30) DEFAULT NULL,
  `interests` char(45) DEFAULT NULL,
  PRIMARY KEY (`CUSTOMER_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `behaviour_analytics`
--

LOCK TABLES `behaviour_analytics` WRITE;
/*!40000 ALTER TABLE `behaviour_analytics` DISABLE KEYS */;
INSERT INTO `behaviour_analytics` VALUES ('CST001','Male','28','650000','78','Mumbai','85.50','Card','Google Search','12.00','Gold','Cricket, Photography'),('CST002','Female','34','1200000','92','Delhi','91.25','UPI','Instagram','5.50','Platinum','Yoga, Gardening'),('CST003','Female','22','350000','45','Bangalore','60.00','UPI','Direct','45.10','Silver','Gaming, Reading'),('CST004','Male','45','1800000','60','Chennai','74.00','NetBank','Email Campaign','22.30','Platinum','Travel, Cooking'),('CST005','Female','31','850000','80','Hyderabad','88.70','Card','Google Search','18.90','Gold','Movies, Fitness');
/*!40000 ALTER TABLE `behaviour_analytics` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employees`
--

DROP TABLE IF EXISTS `employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employees` (
  `EMP_ID` char(6) NOT NULL,
  `FIRST_NME` char(25) DEFAULT NULL,
  `LAST_NME` char(25) DEFAULT NULL,
  `ROLE` char(15) DEFAULT NULL,
  `SHIFT` char(10) DEFAULT NULL,
  `contact_nmbr` char(10) DEFAULT NULL,
  `store_id` char(5) DEFAULT NULL,
  PRIMARY KEY (`EMP_ID`),
  UNIQUE KEY `STORE_ID` (`store_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employees`
--

LOCK TABLES `employees` WRITE;
/*!40000 ALTER TABLE `employees` DISABLE KEYS */;
INSERT INTO `employees` VALUES ('EMP001','Aarav','Sharma','Manager','Day','987654321','ST011'),('EMP002','Vihaan','Patel','Cashier','Day','876543210','ST012'),('EMP003','Ananya','Iyer','Associate','Night','765432109','ST013'),('EMP004','Sai','Reddy','Supervisor','Night','654321098','ST014'),('EMP005','Ishaan','Gupta','Security','Day','543210987','ST015');
/*!40000 ALTER TABLE `employees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stores`
--

DROP TABLE IF EXISTS `stores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stores` (
  `CATEGORY` char(15) DEFAULT NULL,
  `floor` char(10) DEFAULT NULL,
  `unit_nmbr` char(15) NOT NULL,
  `LEASE_START` date DEFAULT NULL,
  `LEASE_END` date DEFAULT NULL,
  `rent` char(10) DEFAULT NULL,
  `contact_person` char(50) DEFAULT NULL,
  `contact_nmbr` char(10) DEFAULT NULL,
  PRIMARY KEY (`unit_nmbr`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stores`
--

LOCK TABLES `stores` WRITE;
/*!40000 ALTER TABLE `stores` DISABLE KEYS */;
INSERT INTO `stores` VALUES ('Apparel','1','101','2025-01-01','2030-01-01','50000','Rajesh Kumar','98765432'),('Electronics','1','102','2025-03-15','2028-03-15','75000','Priya Luthra','87654321'),('Groceries','0','103','2024-06-01','2029-06-01','90000','Amit Desai','76543210'),('Footwear','2','201','2026-02-01','2031-02-01','45000','Sunita Rao','65432109'),('Cafe','2','202','2025-09-01','2027-09-01','60000','Vikram Singh','54321098');
/*!40000 ALTER TABLE `stores` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-10-15  0:31:37
