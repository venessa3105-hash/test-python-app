import pickle

SECRET_PASSWORD = "admin123"

def deserialize(data):
    return pickle.loads(data)

def check(password):
    return password == SECRET_PASSWORD
