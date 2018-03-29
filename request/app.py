from flask import Flask,request
import requests
import json
app = Flask(__name__)

@app.route("/get")
def get():
    getData = requests.get("http://127.0.0.1:5000/get?data=apple")
    print getData.text
    return "ok"

@app.route("/post/text")
def postText():
    postText = requests.post('http://localhost:5000/post/text',data="apple")
    print postText.text
    return "ok"

@app.route("/post/json")
def postJson():
    postJson = requests.post('http://localhost:5000/post/json',json={"data":"apple"})
    print json.loads(postJson.text)['data']
    return "ok"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)
