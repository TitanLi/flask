from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/post', methods=['POST'])
def post():
    email = request.form.get('account')
    password = request.form.get('password')
    print "email:"+email+"\tpassword:"+password
    return 'ok'
