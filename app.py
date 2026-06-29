from flask import Flask

app = Flask(__name__)

VERSION = "2.0"

@app.route("/")
def hello() -> str:
    return f"<h1>Hello from OpenShift!</h1><p>Version: {VERSION}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
