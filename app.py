import os
from flask import Flask

app = Flask(__name__)

GREETING = os.environ.get("GREETING", "Hello")
VERSION = "4.0"


@app.route("/")
def hello() -> str:
    return f"<h1>{GREETING} from OpenShift!</h1><p>Version: {VERSION}</p>"


@app.route("/health")
def health() -> tuple[str, int]:
    return "ok", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
