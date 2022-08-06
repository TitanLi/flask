from flask import Flask,request,render_template
import subprocess
import json
import twstock
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    # 殖利率
    dividendYield = requests.get('https://www.twse.com.tw/exchangeReport/BWIBBU_d?response=json&date=20201201&selectType=ALL&_=1646738579135')
    print(dividendYield.data)
    hightDividendYield = []
    for dividendYield_data in dividendYield.data:
        if dividendYield_data[2] > 6:
            hightDividendYield.append(dividendYield_data)
    stock = twstock.Stock('6274')
    stock.fetch_from(2016, 1)
    data = stock.price
    date = stock.date
    dataList = []
    for i in range(len(date)):
        timestamp = int(datetime.timestamp(date[i]))
        print(int(timestamp))
        listElement = []
        listElement.append(timestamp * 1000)
        listElement.append(data[i])
        dataList.append(listElement)
    return json.dumps(dividendYield_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
