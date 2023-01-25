import awsgi
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello', methods=['GET'])
def hello_get():
    return {'msg': 'get method ver.2'}

@app.route('/hello', methods=['POST'])
def hello_post():
    return {'msg': 'post method ver.2'}

def lambda_handler(event, context):
    return awsgi.response(app, event, context)