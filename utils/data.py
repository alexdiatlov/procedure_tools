import math

from datetime import datetime, timedelta

from utils.datetime import utc

ACCELERATION_DEFAULT = 460800
TENDER_PERIOD_TIMEDELTA_DEFAULT = timedelta(days=30)
TENDER_SECONDS_BUFFER = 10


def set_acceleration_data(
        data,
        acceleration=ACCELERATION_DEFAULT,
        tender_period_timedelta=TENDER_PERIOD_TIMEDELTA_DEFAULT):
    data['data']['mode'] = "test"
    data['data']['procurementMethodDetails'] = "quick, accelerator={}".format(acceleration)
    data['data']['submissionMethodDetails'] = "quick(mode:no-auction)"
    tender_period_seconds = int(tender_period_timedelta.total_seconds())
    data['data']['tenderPeriod']['endDate'] = (
        datetime.now() + timedelta(seconds=tender_period_seconds / acceleration + TENDER_SECONDS_BUFFER)
    ).isoformat()
    return data


def set_agreement_period(data):
    data['data']['period']['startDate'] = (
        datetime.now()
    ).isoformat()
    data['data']['period']['endDate'] = (
        datetime.now() + timedelta(days=365*2)
    ).isoformat()
    return data


def get_tender_id(response):
    return response.json()['data']['id']


def get_tender_token(response):
    return response.json()['access']['token']


def get_tender_period_seconds(response):
    tender_period_end = response.json()['data']['tenderPeriod']['endDate']
    tender_period_timedelta = datetime.fromisoformat(tender_period_end) - datetime.now(utc)
    return math.ceil(tender_period_timedelta.total_seconds())


def get_qualification_period_seconds(response):
    qualification_period_end = response.json()['data']['qualificationPeriod']['endDate']
    qualification_timedelta = datetime.fromisoformat(qualification_period_end) - datetime.now(utc)
    return math.ceil(qualification_timedelta.total_seconds())
