from flask import Flask,request,render_template
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import Column ,Integer, String
from form import Loginform,RegisterForm
from sqlalchemy.exc import IntegrityError

app=Flask(__name__)
db=SQLAlchemy(app)
app.config['SECRET_KEY']='sfsfsf'
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://fateme:1378@localhost:3306/flaskdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class User(db.Model):
    __tablename__= 'users'
    id=Column(Integer,primary_key=True)
    username=Column(String(32),nullable=False,unique=True)
    password=Column(String(128),nullable=False)


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
            new_user=User()
            new_user.username=username
            new_user.password=password
            db.session.add(new_user)
            db.session.commit()
            return 'User added :)'
        except IntegrityError:
            db.session.rollback()
            return render_template('register.html',register_form=register_form,error='User is exist')
    else:
        return render_template('register.html',register_form=register_form,error='Confirm password error')


@app.route('/login/',methods=['POST'])
def login():
    login_form=Loginform(request.form)
    if login_form.validate_on_submit():
        username=request.form.get('username')
        password=request.form.get('password')
        user=User.query.filter(User.username==username,User.password==password).first()
        if not user:
            return render_template('login.html',login_form=login_form,error='invalid username or password !!!!')
        return render_template('doshboard.html',user=user.username)
    return render_template('login.html',login_form=login_form,error='invalid username or password !!!!')