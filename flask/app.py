from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/poulet")
def hello_poulet():
    return "<h1>Hello Poulet</h1>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)