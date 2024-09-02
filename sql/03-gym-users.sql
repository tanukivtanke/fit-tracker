
alter table user add column color text not null default '';
alter table user add column image_gym text not null default '';

update user set color = '785f6f' where username = 'tanuki';
update user set color = '4f6e75' where username = '2493';

update user set image_gym = 'tanuki.jpg' where username = 'tanuki';
update user set image_gym = '2493.png' where username = '2493';








