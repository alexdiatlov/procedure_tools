import json
import os

from procedure_tools.utils.file import get_project_dir


def sort_data_json():
    for root, dirs, files in os.walk(os.path.join(get_project_dir(), "data")):
        for file in files:
            try:
                with open(os.path.join(root, file), "r") as f:
                    lines = json.loads(f.read())
                with open(os.path.join(root, file), "w") as f:
                    f.write(json.dumps(lines, sort_keys=True, indent=2, ensure_ascii=False).encode('utf8'))
            except ValueError:
                pass


if __name__ == "__main__":
    sort_data_json()
