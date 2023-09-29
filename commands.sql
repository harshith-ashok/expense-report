create table users
(
    id int primary key,
    name varchar(20) not null unique,
    pwd varchar(128)
);

create table data
(
    id int primary key,
    budget int not null,
    method varchar(20) default 'cash',
    category varchar(30),
    sub_category varchar(30) default 'N/A',
    due date,
    FOREIGN KEY (id) REFERENCES users(id)
)

drop database if EXISTS users;