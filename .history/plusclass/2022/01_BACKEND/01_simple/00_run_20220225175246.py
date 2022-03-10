from flask import Flask 

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"

app.run(host='0000:4000:0000:0000:0000:0000:0000:0000', port=80)