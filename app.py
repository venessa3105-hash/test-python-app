from flask import Flask, request
import os
import hashlib
import subprocess
def insecure_command(cmd):
    subprocess.run(cmd, shell=True)
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

