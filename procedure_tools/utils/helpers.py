import datetime

from procedure_tools.utils.date import fix_datetime, get_now

DEFAULT_ACCELERATION = 1


def from_now(
    acceleration=DEFAULT_ACCELERATION,
    client_timedelta=None,
    isoformat=False,
    **kwargs,
):
    now = get_now()
    if client_timedelta:
        now = fix_datetime(now, client_timedelta)
    td = datetime.timedelta(**kwargs)
    if acceleration:
        td /= acceleration
    return (now + td).isoformat()


def from_now_iso(
    acceleration=DEFAULT_ACCELERATION,
    client_timedelta=None,
    **kwargs,
):
    return from_now(
        acceleration=acceleration,
        client_timedelta=client_timedelta,
        isoformat=True,
        **kwargs,
    )
