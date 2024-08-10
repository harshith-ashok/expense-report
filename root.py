# MySQL Connector
import mysql.connector as sql

# Random for id generator
import random

con = sql.connect(user='****', password='******',host='localhost',auth_plugin='mysql_native_password')

cur = con.cursor()

cur.execute("use test;")
# print(sub_list)



def add_user():

    # name
    name = input('Name of the Person (no caps): ')

    # password
    password = input('Password: ')

    # budget
    budget = int(input('Annual Income :'))

    # method
    payment = int(input('Payment Method:\n1. Cash\n2. Card \n3. Transfer\n: '))
    pay = ['Cash', 'Card', 'Transfer']
    pay_select = pay[payment - 1]

    # Category
    cur.execute('select * from categories order by cat_id;')
    cat = cur.fetchall()

    for i in range(len(cat)):
        print(i+1, cat[i][1], sep=' : ')
    c = int(input('Category: '))

    # Sub Category
    cur.execute("select sub_id,sub_name from sub_categories where cat_id={id}".format(id=c))
    sub_list = cur.fetchall()

    cur.execute('select * from sub_categories;')
    sub = cur.fetchall()

    print('')

    for i in range(len(sub_list)):
        print(sub_list[i][0],sub_list[i][1],sep=' : ')

    s = int(input('Sub Category: '))

    # cycle
    cyc_in = int(input('''
Cycle:
    1. Yealry
    2. Monthly
    3. Quarterly
    4. Weekly
: '''))
    cyc = ['Yearly', 'Monthly', 'Quarterly', 'Weekly']
    cyc_select = cyc[cyc_in - 1]

    # TODO: Reciept
    payee = input('Payee: ')

    cur.execute("insert into users(user_id, user_name,pwd_hash) values(1,'%s','%s')" % (name,hash(password)))
    cur.execute("insert into master(user_id,income,method,cycle,reciept,payee,cat_id,sub_id) values(1,{budget},'{pay_method}','{cycle}','nan','{payee}',{cat_id},{sub_id})".format(budget=budget, pay_method=pay_select,cycle=cyc_select,payee=payee,cat_id=c,sub_id=s))
    print('Updated !')
    con.commit()
add_user()
