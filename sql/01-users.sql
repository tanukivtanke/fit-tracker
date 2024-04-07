create table if not exists user (
    id integer primary key autoincrement,
    username text
);

insert into user (username) values ('tanuki');
insert into user (username) values ('2493');
