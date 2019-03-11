import math

from datetime import datetime, timedelta

ACCELERATION_DEFAULT = 460800
TENDER_PERIOD_TIMEDELTA_DEFAULT = timedelta(days=30)
TENDER_SECONDS_BUFFER = 10


def get_period_delta(
        acceleration=ACCELERATION_DEFAULT,
        period_timedelta=TENDER_PERIOD_TIMEDELTA_DEFAULT,
        seconds_buffer=TENDER_SECONDS_BUFFER):
    period_seconds = int(period_timedelta.total_seconds())
    return timedelta(seconds=period_seconds / acceleration + seconds_buffer)


def set_acceleration_data(
        data,
        acceleration=ACCELERATION_DEFAULT,
        period_timedelta=TENDER_PERIOD_TIMEDELTA_DEFAULT):
    if 'data' in data:
        data['data']['mode'] = "test"
        data['data']['procurementMethodDetails'] = "quick, accelerator={}".format(acceleration)
        if data['data'].get('procurementMethod') != 'limited':
            data['data']['submissionMethodDetails'] = "quick(mode:no-auction)"

        period_delta = get_period_delta(acceleration, period_timedelta)

        now = datetime.now()
        if 'enquiryPeriod' in data['data'] and 'tenderPeriod' in data['data']:
            data['data']['enquiryPeriod']['endDate'] = (now + period_delta).isoformat()
            data['data']['tenderPeriod']['endDate'] = (now + 2 * period_delta).isoformat()
        elif 'tenderPeriod' in data['data']:
            data['data']['tenderPeriod']['endDate'] = (now + period_delta).isoformat()
    return data


def set_tender_period_data(
        data,
        acceleration=ACCELERATION_DEFAULT,
        period_timedelta=TENDER_PERIOD_TIMEDELTA_DEFAULT):
    period_delta = get_period_delta(acceleration, period_timedelta,
                                    seconds_buffer=math.ceil(TENDER_SECONDS_BUFFER * 2.5))
    if 'data' in data and 'tenderPeriod' in data['data']:
        data['data']['tenderPeriod']['endDate'] = (datetime.now() + period_delta).isoformat()
    return data


def set_agreement_period(data):
    now = datetime.now()
    data['data']['period']['startDate'] = now.isoformat()
    data['data']['period']['endDate'] = (now + timedelta(days=365*2)).isoformat()
    return data


def get_tender_id(response):
    return response.json()['data']['id']


def get_tender_token(response):
    return response.json()['access']['token']


def get_tender_next_check(response):
    return response.json()['data']['next_check']


def get_tender_next_check(response):
    return response.json()['data']['next_check']


def get_procurement_method_type(response):
    return response.json()['data']['procurementMethodType']
