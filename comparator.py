from flask import Flask, request
import jsondiff as jd
from jsondiff import diff

app = Flask(__name__)

@app.route('/ping', methods = ['GET'])
def ping():
    return "pong"

@app.route('/diff', methods = ['POST'])
def difference():
    data = request.json
    return diff(data['first'], data['second'], marshal=True)

if __name__ == '__main__':
    app.run(debug = True, port=8099)
