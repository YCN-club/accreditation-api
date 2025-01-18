import os
import json


def load_form_data(slug, forms_dir="forms"):
    file_path = os.path.join(forms_dir, f"{slug}.json")
    if not os.path.isfile(file_path):
        raise FileNotFoundError("Form not found")
    with open(file_path, "r") as file:
        return json.load(file)
