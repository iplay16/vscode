create DATABASE herogame
-- SQLite
SELECT * FROM COMPANY LIMIT 3

create DATABASE herogame DEFAULT CHARACTER SET 'utf8'
DEFAULT COLLATE 'utf8_general_ci';---不区分大小写
show create database herogame;


show variables like '%commit%';
SET autocommit=OFF;
show variables like '%commit%';


use herogame
create table usertableofheros(
    userid int PRIMARY KEY AUTO_INCREMENT,
    username varchar(20) NOT NULL,
    password varchar(20) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET='utf8'
show create table usertableofheros

insert into usertableofheros (username,password) values("mike","223");
select * from usertableofheros;

create table heros(
    heroid int PRIMARY KEY AUTO_INCREMENT,
    heroname varchar(20),
    herolevel int,
    userid int,
    FOREIGN KEY(userid) REFERENCES usertableofheros(userid) 
)ENGINE=InnoDB DEFAULT CHARSET='utf8'

insert into heros(heroname,herolevel,userid) values("yuji",2,2)
select * from heros;

create table weapons(
    weaponid int PRIMARY KEY AUTO_INCREMENT,
    weaponname varchar(20),
    weaponproperty varchar(20),
    weaponval   varchar(20),
    heroid int,
    FOREIGN KEY(heroid) REFERENCES heros(heroid)
)ENGINE=InnoDB DEFAULT CHARSET='utf8'

insert into weapons (weaponname,weaponproperty,weaponval,heroid) values("yuanhong","gongji","300",2)
update weapons set weaponval=400 where heroid=2



--weaponsbyheror:
select weaponid,weaponname,weaponproperty,weaponval,heroid from weapons where heroid=%;

--weaponsbyuser:
select weaponid,weaponname,weaponproperty,weaponval,heroid from weapons w where w.heroid in (select heroid from heros h where h.userid=%s)

--join
select weaponid,weaponname,weaponproperty,weaponval,heroid,h.userid from weapons w right outer join heros h on w.heroid=h.herosid 