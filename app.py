from flask import Flask, request
import os
import hashlib

app = Flask(__name__)

API_KEY = "1234567890abcdef"

@app.route("/")
def home():
    return "Test Application"

@app.route("/run")
def run():
    cmd = request.args.get("cmd")
    return os.popen(cmd).read()

@app.route("/hash")
def weak_hash():
    password = request.args.get("password")
    return hashlib.md5(password.encode()).hexdigest()

if __name__ == "__main__":
    app.run(debug=True)
@app.route("/eval")
def eval_input():
    user_input = request.args.get("code")
    return str(eval(user_input))
