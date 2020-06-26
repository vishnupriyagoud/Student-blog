CREATE TABLE `blogs` (
  `sno` int NOT NULL AUTO_INCREMENT,
  `rollno` int NOT NULL,
  `name` varchar(60) NOT NULL,
  `post_date` datetime NOT NULL,
  `post_title` varchar(100) NOT NULL,
  `post_content` varchar(400) NOT NULL,
  `reported_user` int DEFAULT '0',
  PRIMARY KEY (`sno`),
  KEY `rollno_user_idx` (`rollno`),
  CONSTRAINT `rollno_user` FOREIGN KEY (`rollno`) REFERENCES `users` (`rollno`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci