from copy import deepcopy
import json
import os
from pathlib import Path
import standards


def notice_field_changes(old_criteria, new_criteria, source_name, related_item=None):
    """Log all field changes between old and new criteria"""
    changes = []

    # Check top-level fields
    for field in ["title", "description", "source"]:
        if old_criteria.get(field) != new_criteria.get(field):
            changes.append(
                f"  {field}: '{old_criteria.get(field)}' -> '{new_criteria.get(field)}'"
            )

    # Check legislation changes
    old_leg = old_criteria.get("legislation", [])
    new_leg = new_criteria.get("legislation", [])
    if old_leg != new_leg:
        changes.append("- legislation updated")

    # Check requirement groups
    old_groups = old_criteria.get("requirementGroups", [])
    new_groups = new_criteria.get("requirementGroups", [])

    for group_index, (old_group, new_group) in enumerate(zip(old_groups, new_groups)):
        if old_group.get("description") != new_group.get("description"):
            changes.append(
                f"- group {group_index} description: '{old_group.get('description')}' -> '{new_group.get('description')}'"
            )

        old_reqs = old_group.get("requirements", [])
        new_reqs = new_group.get("requirements", [])

        for req_index, (old_req, new_req) in enumerate(zip(old_reqs, new_reqs)):
            for field in ["title", "description", "dataType", "expectedValue"]:
                if old_req.get(field) != new_req.get(field):
                    changes.append(
                        f"- requirement {group_index}.{req_index} {field}: '{old_req.get(field)}' -> '{new_req.get(field)}'"
                    )

    if changes:
        print(f"\nChanges in criteria from {source_name}:")
        print(f"- classification.id: {new_criteria['classification']['id']}")
        if related_item:
            print(f"- relatedItem: {related_item}")
        for change in changes:
            print(change)
    else:
        print(f"\nNo field changes in criteria from {source_name}")
        print(f"- classification.id: {new_criteria['classification']['id']}")
        if related_item:
            print(f"- relatedItem: {related_item}")


def update_criteria_from_json(data, source_data, source_name):
    for criteria in data["data"]:
        original_criteria = criteria.copy()

        # Find matching article
        matching_article = None
        for standards_criterion in source_data:
            if standards_criterion.get("classification", {}).get("id") == criteria.get(
                "classification", {}
            ).get("id"):
                matching_article = deepcopy(
                    standards_criterion
                )  # Make a copy to not modify the original
                break

        if matching_article:
            # Store original fields
            relates_to = criteria.get("relatesTo")
            related_item = criteria.get("relatedItem")

            # Store ALL requirement IDs in order
            original_ids = []
            for group in criteria.get("requirementGroups", []):
                for req in group.get("requirements", []):
                    if "id" in req:
                        original_ids.append(req["id"])

            # Update criteria with standard data
            criteria.clear()
            criteria.update(matching_article)

            # Restore original fields
            if relates_to:
                criteria["relatesTo"] = relates_to
            if related_item:
                criteria["relatedItem"] = related_item

            # Restore original IDs in same order
            id_index = 0
            for group in criteria.get("requirementGroups", []):
                for req in group.get("requirements", []):
                    if id_index < len(original_ids):
                        req["id"] = original_ids[id_index]
                        id_index += 1

            # Log changes
            notice_field_changes(original_criteria, criteria, source_name, related_item)


def process_json_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if "data" not in data:
        return {}  # Return empty dict instead of None

    if "criteria_create" in file_path.name:
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
            "criteria/similar_contracts.json",
            "criteria/tender_guarantee.json",
        ]

        # Process each source file
        for source_file in source_files:
            try:
                source_data = standards.load(source_file)
                update_criteria_from_json(data, source_data, source_file)
            except Exception as e:
                print(f"\nError processing {source_file}: {str(e)}")

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if "criteria_create" in file and file.endswith(".json"):
                file_path = Path(root) / file
                print(f"\nProcessing criteria: {file_path}")
                process_json_file(file_path)


def notice_changes(title_changes, source_name):
    if title_changes:
        print(f"\nChanges from {source_name}:")
        for old_title, new_title in title_changes.items():
            print(f"- Changed: '{old_title}' -> '{new_title}'")
    else:
        print(f"\nNo changes from {source_name}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Update criteria and responses from article_17.json"
    )
    parser.add_argument("root_dir", help="Root directory containing the files")
    args = parser.parse_args()
    process_directory(args.root_dir)
