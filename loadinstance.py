import json

def load_instance(file):
    with open(file, "r") as f:
        return json.load(f)