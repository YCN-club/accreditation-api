import os
import json

from sanic.log import logger

def load_form_data(slug):
    file_path = f"./forms/{slug}.json"
    if not os.path.isfile(file_path):
        raise FileNotFoundError("Form not found")
    with open(file_path, "r") as file:
        return json.load(file)
