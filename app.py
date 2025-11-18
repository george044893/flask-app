import os
import socket
from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    hostname = socket.gethostname()
    return f"You're home now on {hostname} of version 2!"
@app.route('/hello-world')
def hello_world():
    return 'Hello World'

if __name__ == "__main__":
    app.run(debug=True)