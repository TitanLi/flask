from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/post', methods=['POST'])
def post():
    if not request.json:
        abort(400)
    print request.json
    return json.dumps(request.json)
