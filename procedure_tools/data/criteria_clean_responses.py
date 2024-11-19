import json
import os
from pathlib import Path


def sort_response_fields(data):
    for item in data["data"]:
        ordered_item = {}
        if "requirement" in item:
            ordered_item["requirement"] = {"id": item["requirement"]["id"]}
        if "value" in item:
            ordered_item["value"] = item["value"]
        if "evidences" in item:
            ordered_item["evidences"] = item["evidences"]

        item.clear()
        item.update(ordered_item)


def clean_response(data):
    # First remove unwanted fields
    for item in data["data"]:
        # Remove title and description if they exist
        if "title" in item:
            del item["title"]
        if "description" in item:
            del item["description"]

        # Also check inside requirement object
        if "requirement" in item:
            if "title" in item["requirement"]:
                del item["requirement"]["title"]
            if "description" in item["requirement"]:
                del item["requirement"]["description"]

    # Then sort fields
    sort_response_fields(data)


def process_json_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if "data" not in data:
        return

    if "bid_res_post" in file_path.name:
        clean_response(data)
        print(f"Cleaned and sorted response fields in: {file_path}")

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if "bid_res_post" in file and file.endswith(".json"):
                file_path = Path(root) / file
                process_json_file(file_path)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Clean and sort response fields")
    parser.add_argument("root_dir", help="Root directory containing the files")
    args = parser.parse_args()
    process_directory(args.root_dir)
