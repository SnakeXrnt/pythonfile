from flask import Flask 

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"

@app.route('/anas')
def anas():
    return "Ananas Botack"

@app.route('html')
def mo

app.run(debug=True)


