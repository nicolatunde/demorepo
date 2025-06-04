create table nico(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name text,
    email_address text not null unique,
    user_name text not null unique,
    password text 
);
insert into nico(name,email_address,user_name,password) values
    ('dada','dadatunde44@gmail.com','nko44','anythings@33'),
    ('akin williams','akinwale44@yahoo.com','akinbol44','passworsecreet44@');
-- select * from nico;

update nico set password = 'ontherun44' where id = 1;
-- select * from nico;

-- select * from nico where name like 'da%';

delete from nico where id = 1 ;

select * from nico;

drop table nico;

select * from nico;

