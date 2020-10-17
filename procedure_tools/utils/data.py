import math

from datetime import datetime, timedelta
from dateutil import tz

TZ = tz.gettz("Europe/Kiev")

ACCELERATION_DEFAULT = 460800
TENDER_PERIOD_TIMEDELTA_DEFAULT = timedelta(days=30)
TENDER_SECONDS_BUFFER = 10

SUBMISSION_QUICK = 'quick'
SUBMISSION_QUICK_NO_AUCTION = 'quick(mode:no-auction)'
SUBMISSION_QUICK_FAST_FORWARD = 'quick(mode:fast-forward)'

DATETIME_MASK = "XXXX-XX-XXTXX:XX+XX:XX"

SUBMISSIONS = [
    SUBMISSION_QUICK,
    SUBMISSION_QUICK_NO_AUCTION,
    SUBMISSION_QUICK_FAST_FORWARD
]


def get_period_delta(
    acceleration=ACCELERATION_DEFAULT,
    period_timedelta=TENDER_PERIOD_TIMEDELTA_DEFAULT,
    seconds_buffer=TENDER_SECONDS_BUFFER,
):
    period_seconds = int(period_timedelta.total_seconds())
    return timedelta(seconds=period_seconds / acceleration + seconds_buffer)


def set_mode_data(data):
    if "data" in data:
        data["data"]["mode"] = "test"


def set_acceleration_data(
    data,
    acceleration=ACCELERATION_DEFAULT,
    period_timedelta=TENDER_PERIOD_TIMEDELTA_DEFAULT,
    submission=SUBMISSION_QUICK_NO_AUCTION
):
    try:
        data["data"]["procurementMethodDetails"] = "quick, accelerator={}".format(acceleration)
        if data["data"].get("procurementMethod") != "limited":
            data["data"]["submissionMethodDetails"] = submission

        now = datetime.now(TZ)

        period_delta = get_period_delta(
            acceleration, period_timedelta,
            seconds_buffer=math.ceil(TENDER_SECONDS_BUFFER * 2)
        )

        if "tenderPeriod" in data["data"] and "enquiryPeriod" in data["data"]:
            if "startDate" in data["data"]["enquiryPeriod"]:
                if data["data"]["enquiryPeriod"]["startDate"] == DATETIME_MASK:
                    data["data"]["enquiryPeriod"]["startDate"] = now.isoformat()

            if "endDate" in data["data"]["enquiryPeriod"]:
                if data["data"]["enquiryPeriod"]["endDate"] == DATETIME_MASK:
                    data["data"]["enquiryPeriod"]["endDate"] = (now + period_delta).isoformat()

            if "startDate" in data["data"]["tenderPeriod"]:
                if data["data"]["tenderPeriod"]["startDate"] == DATETIME_MASK:
                    data["data"]["tenderPeriod"]["startDate"] = (now + period_delta).isoformat()

            if "endDate" in data["data"]["tenderPeriod"]:
                if data["data"]["tenderPeriod"]["endDate"] == DATETIME_MASK:
                    data["data"]["tenderPeriod"]["endDate"] = (now + 2 * period_delta).isoformat()

        elif "enquiryPeriod" in data["data"]:
            if "startDate" in data["data"]["enquiryPeriod"]:
                if data["data"]["enquiryPeriod"]["startDate"] == DATETIME_MASK:
                    data["data"]["enquiryPeriod"]["startDate"] = now.isoformat()

            if "endDate" in data["data"]["enquiryPeriod"]:
                if data["data"]["enquiryPeriod"]["endDate"] == DATETIME_MASK:
                    data["data"]["enquiryPeriod"]["endDate"] = (now + period_delta).isoformat()

        elif "tenderPeriod" in data["data"]:
            if "startDate" in data["data"]["tenderPeriod"]:
                if data["data"]["tenderPeriod"]["startDate"] == DATETIME_MASK:
                    data["data"]["tenderPeriod"]["startDate"] = now.isoformat()

            if "endDate" in data["data"]["tenderPeriod"]:
                if data["data"]["tenderPeriod"]["endDate"] == DATETIME_MASK:
                    data["data"]["tenderPeriod"]["endDate"] = (now + 2 * period_delta).isoformat()

    except KeyError:
        pass

    return data


def set_agreement_id(data, agreement_id):
    try:
        data["data"]["agreements"] = [{"id": agreement_id}]
    except KeyError:
        pass
    return data


def set_tender_period_data(data, acceleration=ACCELERATION_DEFAULT, period_timedelta=TENDER_PERIOD_TIMEDELTA_DEFAULT):
    try:
        now = datetime.now(TZ)

        if "tenderPeriod" in data["data"]:
            if "startDate" in data["data"]["tenderPeriod"]:
                if data["data"]["tenderPeriod"]["startDate"] == DATETIME_MASK:
                    data["data"]["tenderPeriod"]["startDate"] = now.isoformat()

            if "endDate" in data["data"]["tenderPeriod"]:
                if data["data"]["tenderPeriod"]["endDate"] == DATETIME_MASK:
                    period_delta = get_period_delta(
                        acceleration, period_timedelta,
                        seconds_buffer=math.ceil(TENDER_SECONDS_BUFFER * 2)
                    )
                    data["data"]["tenderPeriod"]["endDate"] = (now + period_delta).isoformat()
    except KeyError:
        pass
    return data


def set_plan_tender_period_data(data, acceleration=ACCELERATION_DEFAULT, period_timedelta=TENDER_PERIOD_TIMEDELTA_DEFAULT):
    try:
        now = datetime.now(TZ)
        if "tenderPeriod" in data["data"]["tender"]:
            if "startDate" in data["data"]["tender"]["tenderPeriod"]:
                if data["data"]["tender"]["tenderPeriod"]["startDate"] == DATETIME_MASK:
                    data["data"]["tender"]["tenderPeriod"]["startDate"] = now.isoformat()

            if "endDate" in data["data"]["tender"]["tenderPeriod"]:
                if data["data"]["tender"]["tenderPeriod"]["endDate"] == DATETIME_MASK:
                    period_delta = get_period_delta(
                        acceleration, period_timedelta,
                        seconds_buffer=math.ceil(TENDER_SECONDS_BUFFER * 2)
                    )
                    data["data"]["tender"]["tenderPeriod"]["endDate"] = (now + period_delta).isoformat()
    except KeyError:
        pass
    return data


def set_agreement_period(data):

    try:
        now = datetime.now(TZ)
        data["data"]["period"]["startDate"] = now.isoformat()
        data["data"]["period"]["endDate"] = (now + timedelta(days=365 * 2)).isoformat()
    except KeyError:
        pass
    return data


def get_id(response):
    return response.json()["data"]["id"]


def get_token(response):
    return response.json()["access"]["token"]


def get_next_check(response):
    return response.json()["data"]["next_check"]


def get_procurement_method_type(response):
    return response.json()["data"]["procurementMethodType"]


def get_submission_method_details(response):
    return response.json()["data"].get("submissionMethodDetails")


def get_complaint_period_end_date(response):
    return [item["complaintPeriod"]["endDate"] for item in response.json()["data"]]


def get_bids_ids(response):
    return [i["bidID"] for i in response.json()["data"]]


def get_items_ids(response):
    return [item["id"] for item in response.json()["data"]["items"]]


def get_ids(response):
    return [item["id"] for item in response.json()["data"]]
