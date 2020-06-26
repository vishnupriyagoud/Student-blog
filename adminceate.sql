CREATE TABLE `admins` (
  `rollno` int NOT NULL,
  `name` varchar(60) NOT NULL,
  `lastlogin` datetime NOT NULL,
  `password` char(40) NOT NULL,
  PRIMARY KEY (`rollno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci