create table if not exists user (
    id integer primary key autoincrement,
    username text,
    image text
);

insert into user (username, image) values ('tanuki', 'img/tanya_cheese.png');
insert into user (username, image) values ('2493', 'img/vovamilk_can.png');


