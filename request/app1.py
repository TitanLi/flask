from flask import Flask,request
import requests
import json
app = Flask(__name__)

@app.route("/aaa")
@app.route("/aaa/")
def aaa():
    data = requests.get('http://localhost:5000/?data=123')
    print data.text
    return "ok"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)
