from contextlib import contextmanager
import os


@contextmanager
def open_file(path, mode='r', encoding='UTF-8', **kwargs):
    try:
        this_dir, this_filename = os.path.split(__file__)
        data_path = os.path.join(this_dir, "data", path)
        file = open(data_path, mode, encoding=encoding, **kwargs)
    except IOError:
        file = open(path, mode, encoding=encoding, **kwargs)
    yield file
    file.close()


@contextmanager
def ignore(*exceptions, handler=lambda: None):
    try:
        yield
    except exceptions:
        handler()
