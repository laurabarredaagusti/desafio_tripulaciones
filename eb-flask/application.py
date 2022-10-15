from flask import Flask, request
import pandas as pd

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return 'API test desafío'

@app.route('/result', methods=['GET'])
def result():
    brand = request.args.get('brand', None)
    result = 'The brand is ' + brand
    return result

app.run()