from flask import Flask,request,render_template

app=Flask(__name__)

data={
    'user':'fateme',
    'pass':'1234'
}

@app.route('/',methods=['GET','POST'])
def index():
    response='Request content<br/>'
    response+=f'Request method: {request.method}<br/>'
    response+=f'Request args: {request.args}<br/>'
    response+=f'Request body data: {request.form}'
    return response


@app.route('/getnames',methods=['GET','POST'])
def gets():
    name=request.args.get['name'] or request.form.get['name'] 
    return name

@app.route('/form',methods=['GET','POST'])
def forms():
    return render_template('forms.html')

@app.route('/login/',methods=['POST'])
def login():
    username=request.form.get('username')
    pas=request.form.get('password')
    if username.lower()==data['user'] and pas==data['pass'] :
        return f'Hello {username}'
    else:
        return 'Incorrect user or pass'
