from flask import Flask,request,render_template

app = Flask(__name__)

# http://127.0.0.1:5000/hello?search=Titan&page=apple
@app.route('/hello')
def hello():
    search = request.args.get("search")
    page = request.args.get("page")
    return search+"\n"+page
