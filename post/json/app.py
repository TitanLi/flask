from flask import Flask,request
import json
app = Flask(__name__)

@app.route('/post', methods=['POST'])
def post():
    # {"a":"apple"}
    # method one
    if not request.json:
        abort(400)
    print request.json['a']

    # json parse
    # method two
    data = request.data
    dataDict = json.loads(data)
    print dataDict['a']

    return json.dumps(request.json)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
