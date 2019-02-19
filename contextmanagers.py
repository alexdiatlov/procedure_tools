import os
import io

from contextlib import contextmanager


@contextmanager
def open_file(path, mode='r', encoding='UTF-8', **kwargs):
    try:
        this_dir, this_filename = os.path.split(__file__)
        data_path = os.path.join(this_dir, "data", path)
        file = io.open(data_path, mode, encoding=encoding, **kwargs)
    except IOError:
        file = io.open(path, mode, encoding=encoding, **kwargs)
    yield file
    file.close()


@contextmanager
def ignore(*exceptions):
    try:
        yield
    except exceptions:
        pass
