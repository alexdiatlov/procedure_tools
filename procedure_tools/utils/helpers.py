import datetime

from procedure_tools.utils.date import get_now


def now(**kwargs):
    acceleration = kwargs.pop("acceleration", 1)
    return (get_now() + (datetime.timedelta(**kwargs) / acceleration)).isoformat()
