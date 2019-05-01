-- SQLite
SELECT * FROM COMPANY LIMIT 3

create table usertableofheros(
    userid INTEGER PRIMARY KEY AUTOINCREMENT,
    username varchar(20) NOT NULL,
    password varchar(20) NOT NULL
)

insert into usertableofheros (username,password) values("mike","223");
select * from usertableofheros;
