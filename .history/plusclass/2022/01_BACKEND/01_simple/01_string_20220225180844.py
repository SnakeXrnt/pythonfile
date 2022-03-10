from flask import Flask 

app = Flask(__name__)


@app.route('/')
def index():
    return "AKU DI RUMAAH"

@app.route('/about')
def anas():
    return ""

@app.route('html')
def more_html():
    return "<h1>Hello, HTML</h1>"

app.run(debug=True)



