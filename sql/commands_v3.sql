create table users
(
    u_id int primary key,
    u_name varchar(20) unique,
    pass varchar(256),
    income int
);

create table cat
(
    c_id int primary key,
    c_name varchar(20)
)

create table sub_cat
(
    s_id int primary key,
    sub_name varchar(20),
    c_id int,
    foreign key (c_id) references cat(c_id)
);

create table user1
(
    u_id int,
    e_id int primary key,
    method varchar(20),
    cycle varchar(20),
    payee varchar(20),
    c_id int,
    s_id int
);

alter table exp add foreign key(u_id) references users(u_id);
alter table exp add foreign key(c_id) references cat(c_id);
alter table exp add foreign key(s_id) references sub_cat(s_id);


CREATE TABLE expenses (
    e_id INT PRIMARY KEY AUTO_INCREMENT,
    u_id INT NOT NULL,
    c_id INT NOT NULL,
    s_id INT NOT NULL,
    pay_id INT NOT NULL,
    cyc_id INT NOT NULL,
    payee VARCHAR
(250) NOT NULL,
    due_date DATETIME DEFAULT now
() NOT NULL,
    payed_date DATETIME DEFAULT now
() NOT NULL,
    r_id int
);
