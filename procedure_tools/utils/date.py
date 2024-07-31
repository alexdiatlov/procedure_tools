import logging
from datetime import datetime, timedelta

from dateutil import parser, tz

DATE_HEADER_FORMAT = "%a, %d %b %Y %H:%M:%S GMT"

TZ = tz.gettz("Europe/Kiev")


def get_now():
    return datetime.now(TZ)


def get_utcnow():
    return datetime.now(tz.tzutc())


def fix_datetime(dt, delta):
    return dt + delta


def parse_date_header(header):
    return datetime.strptime(
        header,
        DATE_HEADER_FORMAT,
    ).replace(tzinfo=tz.tzutc())


def parse_date(datetime_str):
    return parser.parse(datetime_str)


def get_client_timedelta(clients):
    client_timedelta = timedelta(seconds=0)
    for client in clients:
        if client:
            client_timedelta = min(client_timedelta, client.client_timedelta)
    timedelta_string = client_timedelta_string(client_timedelta)
    logging.info(f"Using client time delta with server: {timedelta_string}\n")
    return client_timedelta


def client_timedelta_string(client_timedelta):
    total_seconds = client_timedelta.total_seconds()
    if total_seconds > 1:
        return "{} seconds".format(int(total_seconds))
    return "{} milliseconds".format(int(total_seconds * 1000))
