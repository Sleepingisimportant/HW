USE website;
SHOW TABLES;

CREATE TABLE member(
id BIGINT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(255) NOT NULL,
username VARCHAR(255) NOT NULL,
password VARCHAR(255) NOT NULL,
follower_count INT UNSIGNED NOT NULL,
time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP);


INSERT INTO member(name, username, password, follower_count) VALUES('John', 'test', 'test', 10);
INSERT INTO member(name, username, password, follower_count) VALUES('Mary', 'mary123', 'mary123', 23);
INSERT INTO member(name, username, password, follower_count) VALUES('Ben', 'ben123', 'ben123', 23);
INSERT INTO member(name, username, password, follower_count) VALUES('Peter', 'peter123', 'peter123', 42);
INSERT INTO member(name, username, password, follower_count) VALUES('Will', 'will123', 'will123', 38);
INSERT INTO member(name, username, password, follower_count) VALUES('Bob', 'bob123', 'bob123', 92);

SELECT * FROM member;
SELECT * FROM member ORDER BY time DESC;
SELECT * FROM member ORDER BY time DESC LIMIT 3 OFFSET 1;
SELECT * FROM member WHERE username = 'test';
SELECT * FROM member WHERE username = 'test' and password = 'test';
SET SQL_SAFE_UPDATES = 0;
UPDATE member SET name = 'test2' WHERE username = 'test';
 
SELECT COUNT(*) FROM member;
SELECT SUM(follower_count) FROM member;
SELECT AVG(follower_count) FROM member;


CREATE TABLE message(
id BIGINT PRIMARY KEY AUTO_INCREMENT,
member_id BIGINT NOT NULL REFERENCES member (id),
cintent VARCHAR(255) NOT NULL,
like_count INT UNSIGNED NOT NULL DEFAULT 0,
time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP); 

SELECT * FROM message;

INSERT INTO message(member_id, content, like_count) VALUES(1, 'This is a banana.', 1);
INSERT INTO message(member_id, content, like_count) VALUES(2, 'This is an apple.', 1);
INSERT INTO message(member_id, content, like_count) VALUES(3, 'This is a pen.', 1);
INSERT INTO message(member_id, content, like_count) VALUES(4, 'This is a monkey.', 1);
INSERT INTO message(member_id, content, like_count) VALUES(5, 'This is a table.', 1);
INSERT INTO message(member_id, content, like_count) VALUES(6, 'This is a ship.', 1);
INSERT INTO message(member_id, content, like_count) VALUES(6, 'This is a man.', 6);
INSERT INTO message(member_id, content, like_count) VALUES(6, 'This is a pig.', 12);




SELECT member.name, message.content FROM message INNER JOIN member ON message.member_id=member.id;
SELECT member.name, message.content FROM message INNER JOIN member ON message.member_id=member.id and member.username='test';
SELECT member.name, AVG(like_count) FROM message INNER JOIN member ON message.member_id=member.id and member.username='test' Group By member.name;





