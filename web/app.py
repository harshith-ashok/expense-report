from flask import Flask, render_template, url_for, request, redirect
import mysql.connector as sql
from flask import jsonify
import random as rand
import basehash

# Intialiise
con = sql.connect(user='root', password='P@ssw0rd!12',host='localhost',auth_plugin='mysql_native_password')
cur = con.cursor()
cur.execute('use v4')

app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def root():
    return redirect(url_for('login'))

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        uname = request.form.get('uname')
        passwd = request.form.get('passwd')
        cur.execute("select pass_hash from users where u_name='{uname}'".format(uname=uname))
        pass_to_check = cur.fetchall()
        cur.execute("select u_name from users where u_name='{uname}'".format(uname=uname))
        uname_to_check = cur.fetchall()
        cur.execute("select count(u_id) from users where u_name='{uname}'".format(uname=uname))
        cnt = cur.fetchall()
        if cnt[0][0] == 1 and str(pass_to_check[0][0]) == str(passwd):
            cur.execute("select u_id from users where u_name='{uname}'".format(uname=uname))
            u_id = cur.fetchall()
            cur.execute("select e_id from expenses where u_id={u_id}".format(u_id=u_id[0][0]))
            e_id = cur.fetchall()
            cur.execute("select * from expenses where u_id={u_id}".format(u_id=u_id[0][0]))
            df = cur.fetchall()
            x = []
            for i in range(len(e_id)):
                x.append(i)
            cur.execute("select * from category")
            category = cur.fetchall()
            cur.execute("select * from sub_category")
            sub_category = cur.fetchall()
            cur.execute("select * from income")
            source = cur.fetchall()
            cur.execute("select * from pay_cycle")
            cyc = cur.fetchall()
            cur.execute("select * from pay_type")
            pay_type = cur.fetchall()
            return render_template('dash.html',u_id=pass_to_check[0][0],data=df, category=category,sub_category=sub_category, source=source, cyc=cyc, pay_type=pay_type,e_id=e_id,i=x)
        else:
            return render_template('misc/401.html')

    return render_template('login.html')

@app.route('/dash',methods=['GET','POST'])
def dash(u_id):
    cur.execute('select * from expenses where u_id={u_id}'.format(u_id=u_id))
    df = cur.fetchall()
    return render_template('dash.html',data=df)

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        uname = request.form.get('uname')
        passwd = request.form.get('passwd')
        cur.execute("insert into users(u_name, pass_hash) values('{uname}','{passwd}')".format(uname=uname, passwd=passwd))
        con.commit()
        cur.execute("select u_id from users where u_name='{uname}'".format(uname=uname))
        u_id = cur.fetchall()
        return render_template('dash.html',u_id=u_id)
    return render_template('register.html')



@app.route('/home',methods=['GET','POST'])
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)