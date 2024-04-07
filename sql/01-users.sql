create table if not exists user (
    id integer primary key autoincrement,
    username text
);

insert into user (id, username) values (1, 'tanuki');
insert into user (id, username) values (2, '2493');
