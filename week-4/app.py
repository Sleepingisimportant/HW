from flask import Flask
from flask import request
from flask import render_template
from flask import redirect, url_for
from flask import session
from numpy import require

# create application object
# set static files route
app = Flask(__name__,
            static_folder="public",
            static_url_path="/")

app.secret_key = "any string but secret"


# homepage: Login Page + Squre calculation
# If a user has successfully logged in, he/she cannot access this page, but will be redirected to the success page.
@app.route("/")
def index():
    if 'username' in session:
        return render_template("success.html")
    else:
        return render_template("index.html")


# login section - ID/Password authentication + whether empty or not
# Control session
@app.route("/signin", methods=["POST"])
def signin():
    username = request.form["username"]
    password = request.form["password"]

    if username == "test" and password == "test":
        user = request.args.get("username", "")
        user = username
        session["username"] = user
        return redirect(url_for('member'))
    elif username == "" or password == "":
        err_msg = "請輸入帳號、密碼"
        return redirect(url_for('error', message=err_msg))
    else:
        err_msg = "帳號、或密碼輸入錯誤"
        return redirect(url_for('error', message=err_msg))


# Successfully log in, otherwise return to homepage
@app.route("/member")
def member():
    if 'username' in session:
        return render_template("success.html")
    else:
        return redirect(url_for('index'))


# Error page; If a user has logged in successfully, different error message will be shown.
@app.route("/error")
def error():
    if 'username' in session:
        message = "Oops! You have logged in but something went wrong! Please return to the previous page and try again."
        return render_template("error.html", err_msg=message)

    else:
        message = request.args.get("message", "")
        message = message if message == "請輸入帳號、密碼" or message == "帳號、或密碼輸入錯誤" else "Oops! Something Wrong! Please return to the previous page and try again."
        return render_template("error.html", err_msg=message)


# sign out 
@app.route("/signout")
def signout():
    session.pop('username', None)
    return redirect(url_for('index'))


# Calculate square of the user input integer
@app.route("/square", methods=['POST'])
def calculation():
    num_input = request.form["num_input"]
    return redirect(url_for('calculation_result', num_input=num_input))

# dynamic routing to the result of the calculation
@app.route("/square/<int:num_input>")
def calculation_result(num_input):
    result = pow(int(num_input), 2)
    return render_template("calculation.html", calculation_result=result)


app.run(port=3000)
