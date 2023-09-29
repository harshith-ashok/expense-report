create table users
(
    user_id int primary key auto_increment,
    user_name varchar
(20) not null unique,
    pwd_hash varchar
(128),
);

create table categories
(
    cat_id int primary key,
    cat_name varchar(20) not null unique,
);

create table sub_categories
(
    sub_id int primary key,
    cat_id int,
    sub_name varchar(20) not null unique,
    foreign key (cat_id) references categories(cat_id),
);

create table master
(
    user_id int primary key auto_increment,
    income int not null,
    method varchar
(20),
    cycle varchar
(20),
    reciept varchar
(20),
    payee varchar
(40) not null,
    cat_id int,
    sub_id int,
);

alter table master add foreign key(user_id) references users(user_id);
alter table master add foreign key(cat_id) references categories(cat_id);
alter table master add foreign key(sub_id) references sub_categories(sub_id);
