from flask import Flask
import os
import socket

app = Flask(__name__)


@app.route("/foo")
def foo():
    return "Hello ECR"

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
