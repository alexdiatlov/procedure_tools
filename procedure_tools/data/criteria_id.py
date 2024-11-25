import json
import os
import uuid
from pathlib import Path


def generate_id():
    return uuid.uuid4().hex


def add_ids_to_criteria(data):
    title_to_id = {}

    for criteria in data["data"]:
        for group in criteria.get("requirementGroups", []):
            for requirement in group.get("requirements", []):
                # If requirement already has an ID, just store the mapping
                if "id" in requirement:
                    title_to_id[requirement["title"]] = requirement["id"]
                    print(f"- Using existing ID {requirement['id']} for requirement: '{requirement['title']}'")
                else:
                    # Generate new ID only if one doesn't exist
                    requirement["id"] = generate_id()
                    title_to_id[requirement["title"]] = requirement["id"]
                    print(f"- Added new ID {requirement['id']} to requirement: '{requirement['title']}'")

    return title_to_id


def add_ids_to_responses(data, title_to_id):
    for response in data["data"]:
        if "requirement" in response:
            title = response["requirement"].get("title")
            if title and title in title_to_id:
                response["requirement"]["id"] = title_to_id[title]
                response["requirement"].pop("title", None)
                print(f"- Added ID {title_to_id[title]} to response (removed title: '{title}')")


def process_directory(directory):
    prefixes = ["", "stage2_", "selection_"]
    for prefix in prefixes:
        for root, _, files in os.walk(directory):
            # Process each criteria_create file separately
            for file in files:
                file_clean = "_".join(file.split("_")[1:])
                if file_clean.startswith(f"{prefix}criteria_create") and file_clean.endswith(".json"):
                    criteria_path = Path(root) / file
                    print(f"\nProcessing criteria: {criteria_path}")

                    # Process criteria file and get title_to_id mapping
                    with open(criteria_path, "r", encoding="utf-8") as f:
                        data = json.load(f)
                        if "data" in data:
                            title_to_id = add_ids_to_criteria(data)
                            with open(criteria_path, "w", encoding="utf-8") as f:
                                json.dump(data, f, indent=2, ensure_ascii=False)

                    # Process corresponding bid_res_post files in the same directory
                    if title_to_id:
                        for res_file in os.listdir(root):
                            res_file_clean = "_".join(res_file.split("_")[1:])
                            if res_file_clean.startswith(f"{prefix}bid_res_post") and res_file_clean.endswith(".json"):
                                response_path = Path(root) / res_file
                                print(f"\nProcessing response: {response_path}")
                                with open(response_path, "r", encoding="utf-8") as f:
                                    data = json.load(f)
                                    if "data" in data:
                                        add_ids_to_responses(data, title_to_id)
                                        with open(response_path, "w", encoding="utf-8") as f:
                                            json.dump(data, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Add IDs to criteria and responses")
    parser.add_argument("root_dir", help="Root directory containing the files")
    args = parser.parse_args()
    process_directory(args.root_dir)
