import os
import json


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
                        "id": file_name.removesuffix(".json"),
                        "name": data.get("name"),
                        "description": data.get("description"),
                        "priority": data.get(
                            "priority", 0
                        ),  # Include priority for sorting
                    }
                )
    summaries.sort(key=lambda x: x["priority"])
    for summary in summaries:
        del summary["priority"]  # Remove priority before returning

    return summaries
