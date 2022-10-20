# MySQL Statement Practices

## Table of Contents
* [Part 3](#part-3)
* [Part 4](#part-4)
* [Part 5](#part-5)


## Part 3

    SELECT * FROM member;
![screenshots/3-1](screenshots/3-1.png)

    SELECT * FROM member ORDER BY time DESC;
![screenshots/3-2](screenshots/3-2.png)

    SELECT * FROM member ORDER BY time DESC LIMIT 3 OFFSET 1;
![screenshots/3-3](screenshots/3-3.png)

    SELECT * FROM member WHERE username = 'test';
![screenshots/3-4](screenshots/3-4.png)

    SELECT * FROM member WHERE username = 'test' and password = 'test';
![screenshots/3-5](screenshots/3-5.png)

    SET SQL_SAFE_UPDATES = 0;
UPDATE member SET name = 'test2' WHERE username = 'test';
![screenshots/3-6](screenshots/3-6.png)

 
## Part 4
    SELECT COUNT(*) FROM member;
![screenshots/4-1](screenshots/4-1.png)

    SELECT SUM(follower_count) FROM member;
![screenshots/4-2](screenshots/4-2.png)

    SELECT AVG(follower_count) FROM member;
![screenshots/4-3](screenshots/4-3.png)


## Part 5

    SELECT * FROM message;
![screenshots/5-1](screenshots/5-1.png)

    SELECT member.name, message.content FROM message INNER JOIN member ON message.member_id=member.id;
![screenshots/5-2](screenshots/5-2.png)


    SELECT member.name, message.content FROM message INNER JOIN member ON message.member_id=member.id and member.username='test';
![screenshots/5-3](screenshots/5-3.png)


SELECT member.name, AVG(like_count) FROM message INNER JOIN member ON message.member_id=member.id and member.username='test' Group By member.name;
![screenshots/5-4](screenshots/5-4.png)


