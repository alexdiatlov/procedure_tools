import json
import os
import uuid
from pathlib import Path

import standards


def add_criteria(data):
    # Load article 16 criteria using standards
    article_16_data = standards.load("criteria/article_16.json")

    # Track existing classification IDs
    existing_ids = {item.get("classification", {}).get("id") for item in data["data"]}

    # Track newly added requirement IDs
    added_requirement_ids = []

    # Add each criterion from article 16 if not exists
    for new_criteria in article_16_data:
        classification_id = new_criteria.get("classification", {}).get("id")
        if classification_id and classification_id not in existing_ids:
            criteria_copy = new_criteria.copy()

            # Add relatesTo tenderer
            criteria_copy["relatesTo"] = "tenderer"

            # Add lorem ipsum to requirement titles and generate IDs if missing
            for group in criteria_copy.get("requirementGroups", []):
                for req in group.get("requirements", []):
                    req["title"] = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
                    if "id" not in req:
                        req["id"] = str(uuid.uuid4().hex)
                    added_requirement_ids.append(req["id"])
                    print(f"Added requirement ID from new article 16 criteria: {req['id']}")

            data["data"].append(criteria_copy)
            existing_ids.add(classification_id)

    return data, added_requirement_ids


def add_response(data, added_requirement_ids):
    if not added_requirement_ids:
        print("\nNo new requirements were added from article_16")
        return data

    print(f"\nRequirement IDs added from article_16: {added_requirement_ids}")

    # Track existing response IDs
    existing_ids = {item.get("requirement", {}).get("id") for item in data["data"]}
    print(f"Existing response IDs: {existing_ids}")

    # Add response for each newly added requirement ID
    responses_added = 0
    for req_id in added_requirement_ids:
        if req_id not in existing_ids:
            new_response = {"requirement": {"id": req_id}, "value": "true"}
            data["data"].append(new_response)
            responses_added += 1
            print(f"Added response for ID: {req_id}")

    print(f"\nTotal responses added: {responses_added}")
    return data


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

                    # Process criteria file
                    added_requirement_ids = []
                    with open(criteria_path, "r", encoding="utf-8") as f:
                        data = json.load(f)
                        if "data" in data:
                            data, new_ids = add_criteria(data)
                            added_requirement_ids.extend(new_ids)
                            with open(criteria_path, "w", encoding="utf-8") as f:
                                json.dump(data, f, indent=2, ensure_ascii=False)

                    # Process corresponding bid_res_post files in the same directory
                    if added_requirement_ids:
                        for res_file in os.listdir(root):
                            res_file_clean = "_".join(res_file.split("_")[1:])
                            if res_file_clean.startswith(f"{prefix}bid_res_post") and res_file_clean.endswith(".json"):
                                response_path = Path(root) / res_file
                                print(f"\nProcessing response: {response_path}")
                                with open(response_path, "r", encoding="utf-8") as f:
                                    data = json.load(f)
                                    if "data" in data:
                                        data = add_response(data, added_requirement_ids)
                                        with open(response_path, "w", encoding="utf-8") as f:
                                            json.dump(data, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Add criteria and responses to JSON files")
    parser.add_argument("root_dir", help="Root directory containing the files")
    args = parser.parse_args()
    process_directory(args.root_dir)
