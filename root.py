# MySQL Connector
import mysql.connector as sql

# Random for id generator
import random

con = sql.connect(user='root', password='P@ssw0rd!12',host='localhost',auth_plugin='mysql_native_password')

cur = con.cursor()


# General Database creation and additional nconfig
cur.execute("drop database if exists expense_report;")
cur.execute("create database expense_report;")
cur.execute("use expense_report;")
cur.execute("create table users(user_id int primary key,name varchar(20) not null unique);")
cur.execute("create table data(user_id int primary key,income int not null,method varchar(20) default 'cash',category varchar(30),sub_category varchar(30) default 'NA',due date,FOREIGN KEY (user_id) REFERENCES users(user_id));")
u_id = 0

def gen_id():
    global u_id
    u_id = random.randrange(100, 300)
    cur.execute('select user_id from users')
    d = cur.fetchall()
    l = []
    for i in range(len(d)):
        l.append(d[i][0])
    for j in l:
        if u_id == j:
            u_id = random.randrange(100, 300)

gen_id()
# Add User
def add_user():
    global n_id
    due = '2006-11-11'
    # name
    name = input('Name of the Person (no caps): ')
    # budget
    budget = int(input('Annual Budget :'))
    # method
    payment = int(input('Payment Method:\n1. Cash\n2. Card \n3. Transfer\n: '))
    # payment list
    pay = ['Cash', 'Card', 'Transfer']
    # category
    cat = int(input('Category:\n1. Automobile\n2. Entertainment\n3. Family\n4. Food\n5. Insurance\n6. Tax\n7. Travel\n8. Utilities\n9. Misc\n: '))
    # category list for insertion
    cat_list = ['Automobile',
        'Entertainment',
        'Family',
        'Food',
        'Insurance',
        'Tax',
        'Travel',
        'Utilities',
        'Misc',
    ]

    sub_list = [
        ['Fuel', 'Maintenance'],
        ['Movies', 'Party', 'Concerts', 'Sports'],
        ['Child Care','Toys', 'Others'],
        ['Breakfast', 'Lunch', 'Dinner', 'Snacks', 'Groceries'],
        ['Automobile','Health', 'Life'],
        ['Property', 'Vehicle', 'Wealth', 'Other'],
        ['Airplane', 'Bus', 'Hotel', 'Taxi', 'Other', 'Water', 'Cable', 'Electricals', 'Gas', 'Internet', 'Telephone'],
        ['NA'],
    ]

    print(sub_list[cat])
    sub_inp = int(input('Sub Category: '))
    sub_val = sub_list[cat][sub_inp - 1]
    print(sub_val)

    val_users = (u_id, name)
    val_data = (u_id, budget, pay[payment], cat_list[cat-1], sub_val, due)

    cur.execute('insert into users values(%s, %s)', val_users)
    cur.execute('insert into data values(%s, %s,%s, %s,%s, %s)', val_data)
    con.commit()

add_user()


