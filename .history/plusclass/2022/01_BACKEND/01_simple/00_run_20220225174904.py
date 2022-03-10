from flask import lask 

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"