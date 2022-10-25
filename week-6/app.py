# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
from flask import render_template
from flask import redirect, url_for
from flask import session

import mysql.connector
from mysql.connector import errorcode


app = Flask(__name__,
            static_folder="public",
            static_url_path="/")

app.secret_key = "any string but secret"


#connect database
try:
    cnx = mysql.connector.connect(user='root', password='',
                                  host='127.0.0.1',
                                  database='website')

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)

cur = cnx.cursor(buffered=True)



def get_comment_content():
    cur.execute("SELECT member.name, message.content FROM message INNER JOIN member ON message.member_id= member.id")
    data=cur.fetchall()
    return data



@app.route("/")
def index():
    if 'username' in session:
     
        return redirect(url_for('member'))

    else:
        return render_template("index.html")



@app.route("/signup", methods=["POST"])
def signup():
    name = request.form["name"]
    username = request.form["username"]
    password = request.form["password"]
    follower_count=0

    cur.execute("SELECT username, COUNT(*) FROM member WHERE username = %s",(username,))

    row_count = cur.rowcount
    if row_count == 0:
        singup_member = ("INSERT INTO member "
                 "(name, username, password, follower_count) "
                 "VALUES (%s, %s, %s, %s)")
        cur.execute(singup_member,(name, username, password, follower_count))
        cnx.commit()
        
        return redirect(url_for('index'))

    else:
        err_msg = "帳號已經被註冊"
        return redirect(url_for('error', message=err_msg))


    
@app.route("/signin", methods=["POST"])
def signin():

    try:
        username = request.form["username"]
        password = request.form["password"]

        cur.execute("SELECT * FROM member WHERE username = %s",(username,))
        
        fetched_data=cur.fetchone()
        id = fetched_data[0]
        name = fetched_data[1]
        pw = fetched_data[3]


        if password==pw:
            session["id"] = id
            session["name"] = name
            session["username"] = username

            return redirect(url_for('member'))

        else:
            err_msg = "帳號、或密碼輸入錯誤"
            return redirect(url_for('error', message=err_msg))

    except:
        err_msg = "帳號、或密碼輸入錯誤"
        return redirect(url_for('error', message=err_msg))





@app.route("/member")
def member():
    if 'username' in session:
        return render_template("success.html", user=session.get("name"), comment_content=get_comment_content())
    else:
        return redirect(url_for('index'))


@app.route("/error")
def error():
    if 'username' in session:
        message = "你已經登錄，請回到上一頁再重新試試。"
        return render_template("error.html", err_msg=message)

    else:
        message = request.args.get("message", "")
        return render_template("error.html", err_msg=message)


@app.route("/message", methods=["POST"])
def message():
    member_id=session.get("id")
    comment=request.form["comment"]
    like_count=0

    insert_comment = ("INSERT INTO message "
                 "(member_id, content, like_count) "
                 "VALUES (%s, %s, %s)")
    cur.execute(insert_comment,(member_id, comment, like_count))
    cnx.commit()
    return redirect(url_for('member'))
    


@app.route("/signout")
def signout():
    session.pop('id', None)
    session.pop('name', None)
    session.pop('username', None)
    session.pop('username', None)
    return redirect(url_for('index'))



app.run(port=3000)



