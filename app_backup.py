from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")
def home():
    return "College AI Assistant is working!"


if __name__ == "__main__":
    app.run(debug=True)
