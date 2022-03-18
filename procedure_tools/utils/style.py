try:
    from colorama import Fore, Style

    FORE_INFO = Fore.CYAN
    FORE_SUCCESS = Fore.GREEN
    FORE_WARNING = Fore.YELLOW
    FORE_ERROR = Fore.RED
    FORE_RESET = Style.RESET_ALL
except ImportError:
    FORE_INFO = ""
    FORE_SUCCESS = ""
    FORE_WARNING = ""
    FORE_ERROR = ""
    FORE_RESET = ""


def fore(msg, fr):
    return fr + msg + FORE_RESET


def fore_info(msg):
    return fore(msg, FORE_INFO)


def fore_success(msg):
    return fore(msg, FORE_SUCCESS)


def fore_warning(msg):
    return fore(msg, FORE_WARNING)


def fore_error(msg):
    return fore(msg, FORE_ERROR)


def fore_status_code(code):
    msg = str(code)
    if 100 <= code < 200:
        return fore_info(msg)
    if 200 <= code < 300:
        return fore_success(msg)
    if 300 <= code < 400:
        return fore_warning(msg)
    if 400 <= code < 500:
        return fore_error(msg)
    if 500 <= code:
        return fore_error(msg)
    return msg
