from flask import Flask, render_template

app = Flask(__name__)

# Index.html, JS bundle, CSS on it, Fetch API on bundle, refactor dir structure to finalize
@app.route("/")
def index():
    return render_template('index.html')