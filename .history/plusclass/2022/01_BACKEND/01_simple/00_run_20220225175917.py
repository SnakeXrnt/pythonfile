from flask import Flask 

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"

app.run(debug=True)

@app.route('/anas')
def anas():
    return