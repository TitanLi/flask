from flask import Flask,request,abort
import json
app = Flask(__name__)

@app.route("/get",methods=["GET"])
def get():
    data = request.args.get("data")
    print data
    return data

@app.route("/post/text",methods=["POST"])
def postText():
    print request.data
    return request.data

@app.route("/post/json",methods=["POST"])
def postJson():
    if not request.json:
        abort(400)
    print request.json["data"]
    return json.dumps(request.json)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
