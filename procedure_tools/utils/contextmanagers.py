import logging
import os
import io

from contextlib import contextmanager

from procedure_tools.utils.handlers import EX_OK
from procedure_tools.utils.style import fore_error


@contextmanager
def open_file(
    path, mode="r", encoding="UTF-8", exit_filename=None, silent_error=False, **kwargs
):
    _, file_name = os.path.split(path)
    logging.info("Processing data file: {}\n".format(file_name))
    try:
        try:
            encoding = encoding if "b" not in mode else None
            file = io.open(path, mode, encoding=encoding, **kwargs)
            yield file
            file.close()
        except IOError as e:
            if not silent_error:
                msg = fore_error(str(e))
                msg += "\n"
                logging.info(msg)
            logging.info("Skipping...\n")
            yield
        except Exception:
            yield
    except Exception:
        pass
    if file_name == exit_filename:
        raise SystemExit(EX_OK)
