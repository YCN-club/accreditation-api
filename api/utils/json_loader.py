import os
import json

from sanic.log import logger


def load_form_data(slug):
    file_path = f"./forms/{slug}.json"
    if not os.path.isfile(file_path):
        raise FileNotFoundError("Form not found")
    with open(file_path, "r") as file:
        return json.load(file)


def list_form_summaries():
    forms_dir = "./forms"
    summaries = []
    for file_name in os.listdir(forms_dir):
        if file_name.endswith(".json") and not file_name.endswith(".schema.json"):
            file_path = os.path.join(forms_dir, file_name)
            with open(file_path, "r") as f:
                data = json.load(f)
                summaries.append(
                    {
                        "name": data.get("name"),
                        "description": data.get("description"),
                    }
                )
    return summaries
