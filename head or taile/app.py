import random
from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result/')
def result():
    h_or_t=random.randint(1,2)
    return render_template('result.html',h_t=h_or_t)