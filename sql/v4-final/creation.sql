-- User
CREATE TABLE users (
    u_id INT PRIMARY KEY AUTO_INCREMENT,
    u_name VARCHAR
(20),
    pass_hash VARCHAR
(255),
    income INT
);

-- Category
CREATE TABLE category
(
    c_id INT PRIMARY KEY,
    c_name VARCHAR(20)
);

-- Sub category
CREATE TABLE sub_category
(
    s_id INT PRIMARY KEY,
    c_id INT,
    s_name VARCHAR(20),
    FOREIGN KEY (c_id)
        REFERENCES cat (c_id)
);

-- Expenses
CREATE TABLE expenses (
    e_id INT PRIMARY KEY AUTO_INCREMENT,
    u_id INT,
    c_id INT,
    s_id INT,
    pay_id INT,
    cyc_id INT,
    payee VARCHAR
(250),
    pay_date DATETIME DEFAULT now
(),
    payed_date DATETIME DEFAULT now
(),
    r_id int
);

-- Receipt
CREATE TABLE receipt (
    r_id INT PRIMARY KEY AUTO_INCREMENT,
    e_id INT,
    r_path VARCHAR
(255),
    FOREIGN KEY
(e_id)
        REFERENCES expenses
(e_id)
);

-- Pay cycle
CREATE TABLE pay_cycle
(
    cyc_id INT PRIMARY KEY,
    cyc_name VARCHAR(20)
);

-- Pay Type
CREATE TABLE pay_type
(
    pay_id INT PRIMARY KEY,
    pay_method VARCHAR(20)
);