from flask import Flask,request,abort
import json
app = Flask(__name__)

@app.route("/post/text",methods=["POST"])
def postText():
    print request.data
    return request.data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
