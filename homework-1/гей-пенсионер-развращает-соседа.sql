-- SQL-команды для создания таблиц

CREATE TABLE north
(
    post_id int PRIMARY KEY,
    title varchar(100) NOT NULL,
    content text
);

INSERT INTO post VALUES (1, 'Happy New Year', '');
INSERT INTO post VALUES
(2, 'My plans for 2023', ''),
(3, 'Lesson learned from 2022', ''),
(4, 'NewPost!', '');

SELECT * FROM north

--CREATE TABLE user_account
--(
--    user_id int PRIMARY KEY,
--    fullname varchar(100) NOT NULL
--);
