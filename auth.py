import json
import os

SECRET_PASSWORD = os.getenv("SECRET_PASSWORD")

def deserialize(data):
    return json.loads(data)

def check(password):
    return password == SECRET_PASSWORD
