from flask import Flask 

app = Flask(__name__)


@app.route('/')
def index():
    return "AK"

@app.route('/anas')
def anas():
    return "Ananas Botack"

@app.route('html')
def more_html():
    return "<h1>Hello, HTML</h1>"

app.run(debug=True)



