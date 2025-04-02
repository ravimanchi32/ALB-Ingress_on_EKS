from flask import Flask
import os
import socket

app = Flask(__name__)


@app.route("/bar")
def foo():
    return "Hello eks"

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
