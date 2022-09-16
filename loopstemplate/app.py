import numbers
from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def index():
    students=['ali','mamad','zahra']
    numbers=[i for i in range(20)]
    return render_template('index.html',students=students,numbers=numbers)
