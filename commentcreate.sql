CREATE TABLE `comments` (
  `comments_id` int NOT NULL AUTO_INCREMENT,
  `rollno` int NOT NULL,
  `name` varchar(60) NOT NULL,
  `comment_body` varchar(400) NOT NULL,
  `comments_date` datetime NOT NULL,
  `post_id` int NOT NULL,
  `active` tinyint NOT NULL DEFAULT '1',
  PRIMARY KEY (`comments_id`),
  KEY `post_id_idx` (`post_id`),
  CONSTRAINT `post_id` FOREIGN KEY (`post_id`) REFERENCES `blogs` (`sno`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci