import argparse
import difflib
import json
import os
from copy import deepcopy
from pathlib import Path
from uuid import uuid4

import standards

dump_kwargs = {
    "sort_keys": True,
    "indent": 2,
    "ensure_ascii": False,
}


def update_criteria_from_standard(data, source_data):
    original_data = deepcopy(data["data"])
    updated_data = data["data"]

    for criteria_index, criteria in enumerate(updated_data):
        original_criteria = original_data[criteria_index]

        # Find matching standard criterion
        matching_criterion = None
        for standards_criterion in source_data:
            if standards_criterion.get("classification", {}).get("id") == criteria.get("classification", {}).get("id"):
                matching_criterion = deepcopy(standards_criterion)  # Make a copy to not modify the original
                break

        if matching_criterion:
            # Update criteria with standard data
            criteria.clear()
            criteria.update(deepcopy(matching_criterion))

            # Restore original fields
            if relates_to := original_criteria.get("relatesTo"):
                criteria["relatesTo"] = relates_to
            if related_item := original_criteria.get("relatedItem"):
                criteria["relatedItem"] = related_item

            # Restore some original fields
            for group_index, group in enumerate(criteria.get("requirementGroups", [])):
                for req_index, req in enumerate(group.get("requirements", [])):
                    # Generate new ID for requirement
                    req["id"] = str(uuid4().hex)

                    # Not implemented
                    req.pop("weight", None)

                    debug = False

                    if req.get("title") == "Кількість реалізованих договорів загалом (без України)":
                        debug = True

                    # Get original group if it exists
                    original_groups = original_criteria.get("requirementGroups", [])
                    if group_index >= len(original_groups):
                        continue
                    original_group = original_groups[group_index]

                    if debug:
                        print(original_groups)

                    # Get original requirement if it exists
                    original_requirements = original_group.get("requirements", [])
                    if req_index >= len(original_requirements):
                        continue
                    original_req = original_requirements[req_index]

                    # Restore original IDs in same order
                    if "id" in original_req:
                        req["id"] = original_req["id"]

                    # Restore original title if it's empty
                    # (fields that supposed to be filled by user)
                    if req["title"] == "":
                        req["title"] = original_req["title"]


def update_criteria(original_data):
    original_data, updated_data = deepcopy(original_data), original_data

    # List of all criteria source files
    source_files = [
        "criteria/LCC.json",
        "criteria/article_16.json",
        "criteria/article_17.json",
        "criteria/contract_guarantee.json",
        "criteria/investors_strategy.json",
        "criteria/local_origin_level.json",
        "criteria/other.json",
        "criteria/period.json",
        "criteria/resident.json",
        "criteria/tender_guarantee.json",
    ]

    # Process each source file
    for source_file in source_files:
        try:
            source_data = standards.load(source_file)
            update_criteria_from_standard(updated_data, source_data)
        except Exception as e:
            print(f"\nError processing {source_file}: {e.__class__.__name__}: {str(e)}")
            raise e

    show_diff(original_data, updated_data)


def show_diff(original_data, updated_data):
    updated_ids = []
    for original_criterion, updated_criterion in zip(original_data["data"], updated_data["data"]):
        # Dump original and updated data to strings
        original_data_str = json.dumps(original_criterion, **dump_kwargs)
        updated_data_str = json.dumps(updated_criterion, **dump_kwargs)
        if original_data_str != updated_data_str:
            diff = difflib.Differ().compare(
                original_data_str.splitlines(),
                updated_data_str.splitlines(),
            )
            print("=" * 100)
            print("\n".join(diff))
            updated_ids.append(updated_criterion["classification"]["id"])

    print("=" * 100)
    if len(updated_ids):
        print(f"Updated {len(updated_ids)} criteria:")
        for id in updated_ids:
            print(id)


def process_directory(directory, readonly=False):
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
                    with open(criteria_path, "r", encoding="utf-8") as f:
                        criteria_data = json.load(f)
                        update_criteria(criteria_data)
                        if not readonly:
                            with open(criteria_path, "w", encoding="utf-8") as f:
                                json.dump(criteria_data, f, **dump_kwargs)
                        else:
                            print("Readonly mode: Not saving changes to criteria file")

                    # Process corresponding bid_res_post files
                    for res_file in os.listdir(root):
                        res_file_clean = "_".join(res_file.split("_")[1:])
                        if res_file_clean.startswith(f"{prefix}bid_res_post") and res_file_clean.endswith(".json"):
                            response_path = Path(root) / res_file
                            print(f"\nProcessing responses: {response_path}")
                            with open(response_path, "r", encoding="utf-8") as f:
                                response_data = json.load(f)
                                if "data" in response_data:
                                    response_data = check_bids_responses(response_data, criteria_data)
                                    if not readonly:
                                        with open(response_path, "w", encoding="utf-8") as f:
                                            json.dump(response_data, f, **dump_kwargs)
                                    else:
                                        print("Readonly mode: Not saving changes to response file")


def check_bids_responses(response_data, criteria_data):
    # Track invalid responses to remove them later
    responses_to_remove = []
    generated_responses = []

    # Create a set of all valid requirement IDs from criteria
    valid_requirement_ids = set()
    for criterion in criteria_data["data"]:
        for group in criterion.get("requirementGroups", []):
            for requirement in group.get("requirements", []):
                valid_requirement_ids.add(requirement.get("id"))

    # Check for responses to non-existent requirements
    for response in response_data["data"]:
        if response.get("requirement", {}).get("id") not in valid_requirement_ids:
            responses_to_remove.append(response)
            print(
                f"Warning: Response found for non-existent requirement ID: {response.get('requirement', {}).get('id')}"
            )

    # Check each criterion
    for criterion in criteria_data["data"]:
        # Skip criteria with source "procuringEntity"
        if criterion.get("source") == "procuringEntity":
            continue

        criterion_responses = []

        # Collect all responses that belong to this criterion's requirements
        for response in response_data["data"]:
            for group in criterion.get("requirementGroups", []):
                for requirement in group.get("requirements", []):
                    if requirement.get("id") == response.get("requirement", {}).get("id"):
                        criterion_responses.append(response)

        if not criterion_responses:
            print(f"Warning: No responses found for criterion {criterion.get('classification', {}).get('id')}")

            # Generate responses for invalid groups
            for group_index, group in enumerate(criterion.get("requirementGroups", [])):
                for requirement in group.get("requirements", []):
                    if "expectedValue" in requirement:
                        print(f"Generating response for requirement {requirement.get('id')}")
                        response_data["data"].append(
                            {"requirement": {"id": requirement.get("id")}, "value": requirement.get("expectedValue")}
                        )
                        generated_responses.append(response_data["data"][-1])
                    elif "expectedValues" in requirement:
                        print(f"Generating response for requirement {requirement.get('id')}")
                        response_data["data"].append(
                            {
                                "requirement": {"id": requirement.get("id")},
                                "value": requirement.get("expectedValues")[0],
                            }
                        )
                        generated_responses.append(response_data["data"][-1])
                    else:
                        print(f"Warning: No expected value found for requirement {requirement.get('id')}")

                # Only one group is expected
                break

            # Skip to next criterion
            continue

        # Group responses by requirementGroup
        responses_by_group = {}
        for response in criterion_responses:
            for group_index, group in enumerate(criterion.get("requirementGroups", [])):
                for requirement in group.get("requirements", []):
                    if requirement.get("id") == response.get("requirement", {}).get("id"):
                        if group_index not in responses_by_group:
                            responses_by_group[group_index] = []
                        responses_by_group[group_index].append(response)

        # Validate responses for each group
        valid_group_found = False
        for group_index, group in enumerate(criterion.get("requirementGroups", [])):
            group_responses = responses_by_group.get(group_index, [])
            required_count = len(group.get("requirements", []))

            if len(group_responses) == required_count:
                if valid_group_found:
                    # If we already found a valid group, these responses are duplicates
                    responses_to_remove.extend(group_responses)
                    print(
                        f"Warning: Multiple complete requirement groups answered for criterion {criterion.get('classification', {}).get('id')}"
                    )
                else:
                    valid_group_found = True
            elif group_responses:
                # Incomplete group responses should be removed
                responses_to_remove.extend(group_responses)
                print(
                    f"Warning: Incomplete responses for requirement group {group_index} in criterion {criterion.get('classification', {}).get('id')}"
                )

        if not valid_group_found:
            print(
                f"Error: No valid complete requirement group responses for criterion {criterion.get('classification', {}).get('id')}"
            )

    print("=" * 100)
    if len(responses_to_remove):
        print(f"Removed {len(responses_to_remove)} responses")
        response_data["data"] = [r for r in response_data["data"] if r not in responses_to_remove]
    if len(generated_responses):
        print(f"Generated {len(generated_responses)} responses")

    return response_data


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Update criteria and responses")
    parser.add_argument("root_dir", help="Root directory containing the files")
    parser.add_argument("--readonly", action="store_true", help="Don't modify any files, just show what would change")
    args = parser.parse_args()

    process_directory(args.root_dir, readonly=args.readonly)
