from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
	time = datetime.now()
	month = time.month
	day = time.day
	if month == 12 and day == 25:
		text="Yes"
	else:
		text = "No"
	return render_template("index.html", text=text)

if __name__ == "__main__":
	app.run()