CREATE DATABASE `class_xii_project` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;


CREATE TABLE `personal` (
  `Name` varchar(20) DEFAULT NULL,
  `Address` varchar(100) DEFAULT NULL,
  `DOB` date DEFAULT NULL,
  `Email` varchar(20) DEFAULT NULL,
  `Mobile` char(10) DEFAULT NULL,
  `RegNo` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`RegNo`)
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `reservation` (
  `RegNo` int NOT NULL,
  `Dates` date DEFAULT NULL,
  `Days` int DEFAULT NULL,
  `Boarding_Point` varchar(1000) DEFAULT NULL,
  `Leaving_Point` varchar(1000) DEFAULT NULL,
  `Members` int DEFAULT NULL,
  PRIMARY KEY (`RegNo`),
  CONSTRAINT `reservation_ibfk_1` FOREIGN KEY (`RegNo`) REFERENCES `personal` (`RegNo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `suite_and_activity` (
  `RegNo` int NOT NULL,
  `Suite_Type` varchar(30) DEFAULT NULL,
  `Activity` varchar(40) DEFAULT NULL,
  `Participants` int DEFAULT NULL,
  `Room_Number` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`Room_Number`),
  KEY `RegNo` (`RegNo`),
  CONSTRAINT `suite_and_activity_ibfk_1` FOREIGN KEY (`RegNo`) REFERENCES `personal` (`RegNo`)
) ENGINE=InnoDB AUTO_INCREMENT=137 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `payment_info` (
  `RegNo` int NOT NULL,
  `Amount` int DEFAULT NULL,
  `Card_Number` varchar(20) DEFAULT NULL,
  `Expiry_Month` int DEFAULT NULL,
  `Expiry_Year` int DEFAULT NULL,
  PRIMARY KEY (`RegNo`),
  CONSTRAINT `payment_info_ibfk_1` FOREIGN KEY (`RegNo`) REFERENCES `personal` (`RegNo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;





