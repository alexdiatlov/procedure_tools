import os
from pathlib import Path

DATA_DIR_DEFAULT = 'aboveThresholdUA'
DATA_SUB_DIR_DEFAULT = 'data'


def get_data_file_path(filename, path):
    return os.path.join(path, filename)


def get_data_all_files(path):
    print(path)
    return os.listdir(path)


def get_project_dir():
    this_dir, this_filename = os.path.split(__file__)
    project_dir, this_dir = os.path.split(this_dir)
    return project_dir


def get_data_path(path):
    default_data_path = get_default_data_path(path)
    data_path = Path(get_default_data_path(path))
    if data_path.is_dir():
        return default_data_path
    return path


def get_default_data_path(data_dir):
    project_dir = get_project_dir()
    return os.path.join(project_dir, DATA_SUB_DIR_DEFAULT, data_dir)


def get_default_data_dirs():
    project_dir = get_project_dir()
    data_path = os.path.join(project_dir, DATA_SUB_DIR_DEFAULT)
    return os.listdir(data_path)
