import math

from datetime import timedelta

from procedure_tools.utils.date import get_now, fix_datetime

ACCELERATION_DEFAULT = 460800
PERIOD_MIN_DEFAULT_TIMEDELTA = timedelta(seconds=0)
TENDER_PERIOD_DEFAULT_TIMEDELTA = timedelta(days=30)
TENDER_PERIOD_MIN_TIMEDELTA = timedelta(seconds=60)
TENDER_PERIOD_MIN_BELOW_TIMEDELTA = timedelta(seconds=180)
TENDER_SECONDS_BUFFER = 20
AGREEMENT_PERIOD_DEFAULT_TIMEDELTA = timedelta(days=365 * 2)

SUBMISSION_QUICK = "quick"
SUBMISSION_QUICK_NO_AUCTION = "quick(mode:no-auction)"
SUBMISSION_QUICK_FAST_FORWARD = "quick(mode:fast-forward)"

DATETIME_MASK = "XXXX-XX-XXTXX:XX+XX:XX"

SUBMISSIONS = [
    SUBMISSION_QUICK,
    SUBMISSION_QUICK_NO_AUCTION,
    SUBMISSION_QUICK_FAST_FORWARD,
]


def get_period_delta(
    acceleration=ACCELERATION_DEFAULT,
    period_timedelta=TENDER_PERIOD_DEFAULT_TIMEDELTA,
    min_period_timedelta=PERIOD_MIN_DEFAULT_TIMEDELTA,
    seconds_buffer=TENDER_SECONDS_BUFFER,
):
    period_seconds = int(period_timedelta.total_seconds())
    accelerated_period_timedelta = timedelta(
        seconds=period_seconds / acceleration + seconds_buffer
    )
    return max(accelerated_period_timedelta, min_period_timedelta)


def set_mode_data(data):
    data["mode"] = "test"


def set_acceleration_data(
    data,
    acceleration=ACCELERATION_DEFAULT,
    submission=None,
    period_timedelta=TENDER_PERIOD_DEFAULT_TIMEDELTA,
    client_timedelta=timedelta(),
):
    try:
        if submission:
            data["submissionMethodDetails"] = submission

        data["procurementMethodDetails"] = "quick, accelerator={}".format(acceleration)

        now = fix_datetime(get_now(), client_timedelta)

        enquiry_period_delta = get_period_delta(
            acceleration=acceleration,
            period_timedelta=period_timedelta,
            seconds_buffer=math.ceil(TENDER_SECONDS_BUFFER),
        )

        tender_period_delta = get_period_delta(
            acceleration=acceleration,
            period_timedelta=period_timedelta,
            seconds_buffer=math.ceil(TENDER_SECONDS_BUFFER),
            min_period_timedelta=TENDER_PERIOD_MIN_TIMEDELTA,
        )

        if "tenderPeriod" in data and "enquiryPeriod" in data:
            if "startDate" in data["enquiryPeriod"]:
                if data["enquiryPeriod"]["startDate"] == DATETIME_MASK:
                    data["enquiryPeriod"]["startDate"] = now.isoformat()

            if "endDate" in data["enquiryPeriod"]:
                if data["enquiryPeriod"]["endDate"] == DATETIME_MASK:
                    data["enquiryPeriod"]["endDate"] = (
                        now + enquiry_period_delta
                    ).isoformat()

            if "startDate" in data["tenderPeriod"]:
                if data["tenderPeriod"]["startDate"] == DATETIME_MASK:
                    data["tenderPeriod"]["startDate"] = (
                        now + enquiry_period_delta
                    ).isoformat()

            if "endDate" in data["tenderPeriod"]:
                if data["tenderPeriod"]["endDate"] == DATETIME_MASK:
                    data["tenderPeriod"]["endDate"] = (
                        now + enquiry_period_delta + tender_period_delta
                    ).isoformat()

        elif "enquiryPeriod" in data:
            if "startDate" in data["enquiryPeriod"]:
                if data["enquiryPeriod"]["startDate"] == DATETIME_MASK:
                    data["enquiryPeriod"]["startDate"] = now.isoformat()

            if "endDate" in data["enquiryPeriod"]:
                if data["enquiryPeriod"]["endDate"] == DATETIME_MASK:
                    data["enquiryPeriod"]["endDate"] = (
                        now + enquiry_period_delta
                    ).isoformat()

        elif "tenderPeriod" in data:
            if "startDate" in data["tenderPeriod"]:
                if data["tenderPeriod"]["startDate"] == DATETIME_MASK:
                    data["tenderPeriod"]["startDate"] = now.isoformat()

            if "endDate" in data["tenderPeriod"]:
                if data["tenderPeriod"]["endDate"] == DATETIME_MASK:
                    data["tenderPeriod"]["endDate"] = (
                        now + enquiry_period_delta + tender_period_delta
                    ).isoformat()

    except KeyError:
        pass

    return data


def set_tender_period_data(
    period_data,
    acceleration=ACCELERATION_DEFAULT,
    period_timedelta=TENDER_PERIOD_DEFAULT_TIMEDELTA,
    min_period_timedelta=PERIOD_MIN_DEFAULT_TIMEDELTA,
    client_timedelta=timedelta(),
):
    try:
        now = fix_datetime(get_now(), client_timedelta)
        if "startDate" in period_data:
            if period_data["startDate"] == DATETIME_MASK:
                period_data["startDate"] = now.isoformat()
        if "endDate" in period_data:
            if period_data["endDate"] == DATETIME_MASK:
                period_delta = get_period_delta(
                    acceleration=acceleration,
                    period_timedelta=period_timedelta,
                    min_period_timedelta=min_period_timedelta,
                    seconds_buffer=math.ceil(TENDER_SECONDS_BUFFER),
                )
                period_data["endDate"] = (now + period_delta).isoformat()
    except KeyError:
        pass
    return period_data


def set_agreement_period(
    period_data,
    period_timedelta=AGREEMENT_PERIOD_DEFAULT_TIMEDELTA,
    client_timedelta=timedelta(),
):
    try:
        now = fix_datetime(get_now(), client_timedelta)
        period_data["startDate"] = now.isoformat()
        period_data["endDate"] = (now + period_timedelta).isoformat()
    except KeyError:
        pass
    return period_data


def get_id(response):
    return response.json()["data"]["id"]


def get_token(response):
    return response.json()["access"]["token"]


def get_next_check(response):
    return response.json()["data"]["next_check"]


def get_tender_period(response):
    return response.json()["data"].get("tenderPeriod")


def get_procurement_method_type(response):
    return response.json()["data"]["procurementMethodType"]


def get_submission_method_details(response):
    return response.json()["data"].get("submissionMethodDetails")


def get_procurement_entity_kind(response):
    return response.json()["data"].get("procurementEntity", {}).get("kind")


def get_config(response):
    return response.json().get("config", {})


def get_complaint_period_end_dates(response):
    return [item["complaintPeriod"]["endDate"] for item in response.json()["data"]]


def get_contract_period_clarif_date(response):
    return response.json()["data"]["contractPeriod"]["clarificationsUntil"]


def get_contracts_bids_ids(response):
    return [i["bidID"] for i in response.json()["data"]]


def get_items_ids(response):
    return [item["id"] for item in response.json()["data"]["items"]]


def get_ids(response):
    return [item["id"] for item in response.json()["data"]]


def get_contracts_items_ids(response):
    return [
        [item["id"] for item in contract["items"]]
        for contract in response.json()["data"]
    ]
