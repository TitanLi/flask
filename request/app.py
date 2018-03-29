from flask import Flask,request
import requests
import json
app = Flask(__name__)

@app.route("/",methods=["GET"])
def index():
    data = request.args.get("data")
    print data
    return "asd"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
