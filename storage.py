#all read/write functions done here
import json

FILENAME ="task.json"

def load_tasks():
    try:
        with open(FILENAME,"r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

