import argparse
import json
import sys
import math

from datetime import datetime
from dateutil import parser, tz
from time import sleep

from .version import __version__
from .client import TendersApiClient, API_PATH_PREFIX_DEFAULT
from .utils.contextmanagers import ignore, open_file_or_exit
from .utils.file import (
    get_data_file_path,
    get_data_all_files,
    get_default_data_dirs,
    get_data_path,
    DATA_DIR_DEFAULT)
from .utils.data import (
    set_acceleration_data,
    set_agreement_period,
    get_tender_id,
    get_tender_token,
    ACCELERATION_DEFAULT,
    TENDER_SECONDS_BUFFER,
    get_procurement_method_type,
    set_tender_period_data, get_tender_next_check)
from .utils.handlers import (
    response_handler,
    item_get_success_print_handler,
    item_patch_success_print_handler,
    tender_patch_status_success_print_handler,
    tender_check_status_success_print_handler,
    tender_create_success_print_handler,
    bid_create_success_print_handler, item_create_success_print_handler)


def get_bids(client, tender_id):
    while True:
        response = client.get_bids(tender_id)
        if not response.json()['data']:
            sleep(TENDER_SECONDS_BUFFER)
        else:
            response_handler(response, item_get_success_print_handler)
            break
    return response


def patch_agreements_with_contracts(client, tender_id, data_path, tender_token, exit_file_name):
    print("Checking agreements...\n")
    response = get_agreements(client, tender_id)
    agreements_ids = [i['id'] for i in response.json()['data']]
    response = get_tender(client, tender_id)
    items_ids = [i['id'] for i in response.json()['data']['items']]
    print("Check bids...\n")
    response = get_bids(client, tender_id)
    bids_ids = [i['id'] for i in response.json()['data']]
    for agreement_index, agreement_id in enumerate(agreements_ids):
        print("Checking agreement contracts...")

        response = get_agreement_contract(client, tender_id, agreement_id)
        agreement_contracts_ids = [i['id'] for i in response.json()['data']]
        agreement_contracts_related_bids = [i['bidID'] for i in response.json()['data']]

        print("Patching agreement contracts...\n")
        patch_agreement_contract(client, tender_id, agreement_id, agreement_index, agreement_contracts_ids,
                                 bids_ids, agreement_contracts_related_bids, items_ids,
                                 data_path, tender_token, exit_file_name)
    print("Patching agreements...\n")
    patch_agreements(client, tender_id, agreements_ids, data_path, tender_token, exit_file_name)


def patch_agreements(client, tender_id, agreements_ids, data_path, tender_token, exit_file_name):
    for agreement_index, agreement_id in enumerate(agreements_ids):
        path = get_data_file_path('agreement_patch_{}.json'.format(agreement_index), data_path)
        with ignore(IOError), open_file_or_exit(path, exit_filename=exit_file_name) as f:
            agreement_patch_data = json.loads(f.read())
            set_agreement_period(agreement_patch_data)
            client.patch_agreement(tender_id, agreement_id, tender_token, agreement_patch_data,
                                   success_handler=item_patch_success_print_handler)


def patch_agreement_contract(client, tender_id, agreement_id, agreement_index, agreement_contracts_ids,
                             bids_ids, agreement_contracts_related_bids, items_ids,
                             data_path, tender_token, exit_file_name):
    for agreement_contract_index, agreement_contract_id in enumerate(agreement_contracts_ids):
        index = bids_ids.index(agreement_contracts_related_bids[agreement_contract_index])
        data_file = 'agreement_{}_contracts_patch_{}.json'.format(agreement_index, index)
        path = get_data_file_path(data_file, data_path)
        with ignore(IOError), open_file_or_exit(path, exit_filename=exit_file_name) as f:
            agreement_contract_patch_data = json.loads(f.read())
            for item_index, items_id in enumerate(items_ids):
                agreement_contract_patch_data['data']['unitPrices'][item_index]['relatedItem'] = items_id
            client.patch_agreement_contract(tender_id, agreement_id, agreement_contract_id, tender_token,
                                            agreement_contract_patch_data,
                                            success_handler=item_patch_success_print_handler)


def get_agreement_contract(client, tender_id, agreement_id):
    while True:
        response = client.get_agreement_contracts(tender_id, agreement_id)
        if not response.json()['data']:
            sleep(TENDER_SECONDS_BUFFER)
        else:
            response_handler(response, item_get_success_print_handler)
            break
    return response


def get_tender(client, tender_id):
    return client.get_tender(tender_id)


def get_agreements(client, tender_id):
    while True:
        response = client.get_agreements(tender_id)
        if not response.json()['data']:
            sleep(TENDER_SECONDS_BUFFER)
        else:
            response_handler(response, item_get_success_print_handler)
            break
    return response


def patch_tender_qual(client, data_path, tender_id, tender_token, exit_file_name):
    print("Approving awards by switching to next status...\n")
    path = get_data_file_path('tender_patch_qual.json', data_path)
    with ignore(IOError), open_file_or_exit(path, exit_filename=exit_file_name) as f:
        tender_patch_data = json.loads(f.read())
        return client.patch_tender(tender_id, tender_token, tender_patch_data,
                                   success_handler=tender_patch_status_success_print_handler)


def patch_awards(client, tender_id, awards_ids, data_path, tender_token, exit_file_name):
    print("Patching awards...\n")
    for award_index, awards_id in enumerate(awards_ids):
        data_file = 'award_patch_{}.json'.format(award_index)
        path = get_data_file_path(data_file, data_path)
        with ignore(IOError), open_file_or_exit(path, exit_filename=exit_file_name) as f:
            award_patch_data = json.loads(f.read())
            client.patch_award(tender_id, awards_id, tender_token, award_patch_data,
                               success_handler=item_patch_success_print_handler)


def get_awards(client, tender_id):
    print("Checking awards...\n")
    while True:
        response = client.get_awards(tender_id)
        if not response.json()['data']:
            sleep(TENDER_SECONDS_BUFFER)
        else:
            response_handler(response, item_get_success_print_handler)
            break
    return response


def patch_contracts(client, tender_id, awards_ids, data_path, tender_token, exit_file_name):
    print("Patching contracts...\n")
    for contract_index, contract_id in enumerate(awards_ids):
        data_file = 'contract_patch_{}.json'.format(contract_index)
        path = get_data_file_path(data_file, data_path)
        with ignore(IOError), open_file_or_exit(path, exit_filename=exit_file_name) as f:
            contract_patch_data = json.loads(f.read())
            client.patch_contract(tender_id, contract_id, tender_token, contract_patch_data,
                                  success_handler=item_patch_success_print_handler)


def get_contracts(client, tender_id):
    print("Checking contracts...\n")
    while True:
        response = client.get_contracts(tender_id)
        if not response.json()['data']:
            sleep(TENDER_SECONDS_BUFFER)
        else:
            response_handler(response, item_get_success_print_handler)
            break
    return response


def patch_tender_pre(client, data_path, tender_id, tender_token, exit_file_name):
    print("Approving qualifications by switching to next status...\n")
    path = get_data_file_path('tender_patch_pre.json', data_path)
    with ignore(IOError), open_file_or_exit(path, exit_filename=exit_file_name) as f:
        tender_patch_data = json.loads(f.read())
        return client.patch_tender(tender_id, tender_token, tender_patch_data,
                                   success_handler=tender_patch_status_success_print_handler)


def patch_qualifications(client, data_path, tender_id, qualifications_ids, tender_token, exit_file_name):
    print("Patching qualifications...\n")
    for qualification_index, qualification_id in enumerate(qualifications_ids):
        data_file = 'qualification_patch_{}.json'.format(qualification_index)
        path = get_data_file_path(data_file, data_path)
        with ignore(IOError), open_file_or_exit(path, exit_filename=exit_file_name) as f:
            qualification_patch_data = json.loads(f.read())
            client.patch_qualification(tender_id, qualification_id, tender_token, qualification_patch_data,
                                       success_handler=item_patch_success_print_handler)


def get_qualifications(client, tender_id):
    print("Checking qualifications...\n")
    while True:
        response = client.get_qualifications(tender_id)
        if not response.json()['data']:
            sleep(TENDER_SECONDS_BUFFER)
        else:
            response_handler(response, item_get_success_print_handler)
            break
    return response


def create_awards(client, data_path, data_files, tender_id, tender_token, exit_file_name):
    print("Creating awards...\n")
    award_files = []
    for data_file in data_files:
        if data_file.startswith('award_create'):
            award_files.append(data_file)
    for award_file in award_files:
        path = get_data_file_path(award_file, data_path)
        with ignore(IOError), open_file_or_exit(path, exit_filename=exit_file_name) as f:
            award_create_data = json.loads(f.read())
            client.post_award(tender_id, tender_token, award_create_data,
                              success_handler=item_create_success_print_handler)


def create_bids(client, data_path, data_files, tender_id, exit_file_name):
    print("Creating bids...\n")
    bid_files = []
    for data_file in data_files:
        if data_file.startswith('bid_create'):
            bid_files.append(data_file)
    for bid_file in bid_files:
        path = get_data_file_path(bid_file, data_path)
        with ignore(IOError), open_file_or_exit(path, exit_filename=exit_file_name) as f:
            bid_create_data = json.loads(f.read())
            client.post_bid(tender_id, bid_create_data, success_handler=bid_create_success_print_handler)


def create_tender(client, data_path, acceleration, exit_file_name):
    print("Creating tender...\n")
    path = get_data_file_path('tender_create.json', data_path)
    with ignore(IOError), open_file_or_exit(path, exit_filename=exit_file_name) as f:
        tender_create_data = json.loads(f.read())
        set_acceleration_data(tender_create_data, acceleration=acceleration)
        response = client.post_tender(tender_create_data, success_handler=tender_create_success_print_handler)
        return response


def update_tender_period(client, tender_id, tender_token, acceleration):
    data = set_tender_period_data({'data': {'tenderPeriod': {}}}, acceleration=acceleration)
    client.patch_tender(tender_id, tender_token, data)


def wait(date_str, date_info_str=None):
    date_timedelta = parser.parse(date_str) - datetime.now(tz.tzutc())
    delta_seconds = date_timedelta.total_seconds()
    date_seconds = math.ceil(delta_seconds) if delta_seconds > 0 else 0
    info_str = ' for {}'.format(date_info_str) if date_info_str else ''
    print("Waiting {} seconds{} - {}...\n".format(date_seconds, info_str, date_str))
    sleep(date_seconds)


def wait_status(client, tender_id, status, fallback=None):
    print("Waiting for {}...\n".format(status))
    while True:
        response = client.get_tender(tender_id)
        if not response.json()['data']['status'] == status:
            sleep(TENDER_SECONDS_BUFFER)
            if fallback:
                fallback()
        else:
            response_handler(response, tender_check_status_success_print_handler)
            break
    return response


def create_procedure(host, token, url_path, data_path, acceleration, exit_file_name):
    data_path = get_data_path(data_path)
    data_files = get_data_all_files(data_path)

    client = TendersApiClient(host, token, url_path)

    response = create_tender(client, data_path, acceleration, exit_file_name)
    if not response:
        sys.exit(0)
    tender_id = get_tender_id(response)
    tender_token = get_tender_token(response)

    method_type = get_procurement_method_type(response)

    if method_type in (
        'belowThreshold',
    ):
        wait(get_tender_next_check(response), date_info_str='next chronograph check')

        def update_tender_period_fallback():
            update_tender_period(client, tender_id, tender_token, acceleration)

        wait_status(client, tender_id, 'active.tendering', fallback=update_tender_period_fallback)

    if method_type in (
        'closeFrameworkAgreementUA',
        'aboveThresholdUA',
        'aboveThresholdUA.defense',
        'aboveThresholdEU',
        'belowThreshold',
        'esco',
    ):
        create_bids(client, data_path, data_files, tender_id, exit_file_name)

    if method_type in (
        'closeFrameworkAgreementUA',
        'aboveThresholdUA',
        'aboveThresholdUA.defense',
        'aboveThresholdEU',
        'belowThreshold',
        'esco',
    ):
        response = get_tender(client, tender_id)
        wait(get_tender_next_check(response), date_info_str='next chronograph check')

    if method_type in (
        'closeFrameworkAgreementUA',
        'aboveThresholdEU',
        'esco',
    ):
        response = get_qualifications(client, tender_id)
        qualifications_ids = [i['id'] for i in response.json()['data']]
        patch_qualifications(client, data_path, tender_id, qualifications_ids, tender_token, exit_file_name)

    if method_type in (
        'closeFrameworkAgreementUA',
        'aboveThresholdEU',
        'esco',
    ):
        patch_tender_pre(client, data_path, tender_id, tender_token, exit_file_name)

    if method_type in (
        'closeFrameworkAgreementUA',
        'aboveThresholdUA.defense',
        'aboveThresholdEU',
        'belowThreshold',
        'esco',
    ):
        wait_status(client, tender_id, 'active.auction')

    if method_type in (
        'negotiation',
        'negotiation.quick',
        'reporting',
    ):
        create_awards(client, data_path, data_files, tender_id, tender_token, exit_file_name)

    if method_type in (
        'negotiation',
        'negotiation.quick',
        'reporting',
    ):
        wait_status(client, tender_id, 'active')

    if method_type in (
        'closeFrameworkAgreementUA',
        'aboveThresholdUA',
        'aboveThresholdUA.defense',
        'aboveThresholdEU',
        'belowThreshold',
        'negotiation',
        'negotiation.quick',
        'reporting',
        'esco',
    ):
        response = get_awards(client, tender_id)
        awards_ids = [i['id'] for i in response.json()['data']]
        patch_awards(client, tender_id, awards_ids, data_path, tender_token, exit_file_name)

    if method_type in (
        'closeFrameworkAgreementUA',
    ):
        patch_tender_qual(client, data_path, tender_id, tender_token, exit_file_name)

    if method_type in (
        'closeFrameworkAgreementUA',
        'aboveThresholdEU',
        'esco',
    ):
        wait_status(client, tender_id, 'active.awarded')

    if method_type in (
        'aboveThresholdUA',
        'aboveThresholdUA.defense',
        'aboveThresholdEU',
        'belowThreshold',
        'negotiation',
        'negotiation.quick',
        'esco',
    ):
        response = get_awards(client, tender_id)
        awards_complaint_dates = [i['complaintPeriod']['endDate'] for i in response.json()['data']]
        wait(max(awards_complaint_dates), date_info_str='end of award complaint period')

    if method_type in (
        'aboveThresholdUA',
        'aboveThresholdUA.defense',
        'aboveThresholdEU',
        'belowThreshold',
        'negotiation',
        'negotiation.quick',
        'reporting',
        'esco',
    ):
        response = get_contracts(client, tender_id)
        contracts_ids = [i['id'] for i in response.json()['data']]
        patch_contracts(client, tender_id, contracts_ids, data_path, tender_token, exit_file_name)

    if method_type in (
        'closeFrameworkAgreementUA',
    ):
        patch_agreements_with_contracts(client, tender_id, data_path, tender_token, exit_file_name)

    print("Completed.\n")


def main():
    if '--version' in sys.argv:
        print(__version__)
        sys.exit(0)

    parser = argparse.ArgumentParser()
    parser.add_argument('host', help='api host')
    parser.add_argument('token', help='api token')
    parser.add_argument('-a', '--acceleration',
                        help='acceleration multiplier',
                        metavar=str(ACCELERATION_DEFAULT),
                        default=ACCELERATION_DEFAULT,
                        type=int)
    parser.add_argument('-p', '--path',
                        help='api path',
                        metavar=str(API_PATH_PREFIX_DEFAULT),
                        default=API_PATH_PREFIX_DEFAULT)
    parser.add_argument('-d', '--data',
                        help='data files path custom or one of {}'.format(get_default_data_dirs()),
                        metavar=str(DATA_DIR_DEFAULT),
                        default=DATA_DIR_DEFAULT)
    parser.add_argument('-s', '--stop',
                        help='data file name to stop after',
                        metavar='tender_create.json')
    args = parser.parse_args()

    create_procedure(args.host, args.token, args.path, args.data, args.acceleration, args.stop)


if __name__ == "__main__":
    main()
