CREATE TABLE `users` (
  `rollno` int NOT NULL,
  `name` varchar(60) NOT NULL,
  `signup_date` datetime NOT NULL,
  `lastlogin_date` datetime NOT NULL,
  `reported_users` int DEFAULT '0',
  `password` char(40) NOT NULL,
  `block_status` tinyint DEFAULT '1',
  PRIMARY KEY (`rollno`),
  UNIQUE KEY `name_UNIQUE` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci