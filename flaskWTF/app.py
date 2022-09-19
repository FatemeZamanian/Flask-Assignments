from distutils.log import error
import sqlite3
from flask import Flask,render_template,request,g,redirect,url_for
from form import Loginform,RegisterForm

app=Flask(__name__)
app.config['SECRET_KEY']='ssfsfsfs'

def create_db():
    return sqlite3.connect('./db.sqlite')


@app.before_request
def before_request_hook():
    g.db=create_db()
    g.cur=g.db.cursor()

@app.after_request
def after_request_hook(response):
    g.db.close()
    return response


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login_form/')
def login_form():
    login_form=Loginform()
    return render_template('login.html',login_form=login_form)

@app.route('/register_form/')
def register_form():
    register_form=RegisterForm()
    return render_template('register.html',register_form=register_form)

@app.route('/register/',methods=['POST'])
def register():
    register_form=RegisterForm(request.form)
    if register_form.validate_on_submit():
        username=request.form.get('username')
        password=request.form.get('password')
        try:
            g.cur.execute('INSERT INTO users (username,password) VALUES (?,?)',(username,password))
            g.db.commit()
            return 'User added :)'
        except sqlite3.IntegrityError:
            g.db.rollback()
            return render_template('register.html',register_form=register_form,error='User is exist')
    else:
        return render_template('register.html',register_form=register_form,error='Confirm password error')


@app.route('/login/',methods=['POST'])
def login():
    login_form=Loginform(request.form)
    if login_form.validate_on_submit():
        username=request.form.get('username')
        password=request.form.get('password')
        g.cur.execute('SELECT * FROM users WHERE username = ? AND password = ?',(username,password))
        user=g.cur.fetchone()
        if not user:
            return render_template('login.html',login_form=login_form,error='invalid username or password !!!!')
        return render_template('doshboard.html',user=user[1])
    return render_template('login.html',login_form=login_form,error='invalid username or password !!!!')