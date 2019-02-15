import argparse
import json
import sys

from time import sleep

from version import __version__
from client import TendersApiClient, API_PATH_PREFIX_DEFAULT
from contextmanagers import ignore, open_file
from utils.file import (
    get_data_file_path,
    get_data_all_files,
    get_default_data_dirs,
    get_data_path,
    DATA_DIR_DEFAULT)
from utils.data import (
    set_acceleration_data,
    set_agreement_period,
    get_tender_id,
    get_tender_token,
    get_tender_period_seconds,
    ACCELERATION_DEFAULT,
    TENDER_SECONDS_BUFFER, get_qualification_period_seconds)
from handlers import (
    response_handler,
    item_get_success_print_handler,
    item_patch_success_print_handler,
    tender_patch_status_success_print_handler,
    tender_check_status_success_print_handler,
    tender_create_success_print_handler,
    bid_create_success_print_handler)


def patch_tender_awarded(client, data_path, tender_id, tender_token):
    with ignore(IOError), open_file(get_data_file_path('tender_patch_awarded.json', data_path)) as f:
        tender_patch_data = json.loads(f.read())
        return client.patch_tender(tender_id, tender_token, tender_patch_data,
                                   success_handler=tender_patch_status_success_print_handler)


def patch_agreements_with_contracts(client, tender_id, data_path, tender_token):
    response = get_agreements(client, tender_id)
    agreements_ids = [i['id'] for i in response.json()['data']]
    response = get_tender(client, tender_id)
    items_ids = [i['id'] for i in response.json()['data']['items']]
    for agreement_index, agreement_id in enumerate(agreements_ids):
        print("Checking agreement contracts...")

        response = get_agreement_contract(client, tender_id, agreement_id)
        agreement_contracts_ids = [i['id'] for i in response.json()['data']]

        print("Patching agreement contracts...\n")
        patch_agreement_contract(client, tender_id, agreement_id, agreement_index,
                                 agreement_contracts_ids, items_ids,
                                 data_path, tender_token)
    print("Patching agreements...\n")
    patch_agreements(client, tender_id, agreements_ids, data_path, tender_token)


def patch_agreements(client, tender_id, agreements_ids, data_path, tender_token):
    for agreement_index, agreement_id in enumerate(agreements_ids):
        data_file = 'agreement_patch_{}.json'.format(agreement_index)
        with ignore(IOError), open_file(get_data_file_path(data_file, data_path)) as f:
            agreement_patch_data = json.loads(f.read())
            set_agreement_period(agreement_patch_data)
            client.patch_agreement(tender_id, agreement_id, tender_token, agreement_patch_data,
                                   success_handler=item_patch_success_print_handler)


def patch_agreement_contract(client, tender_id, agreement_id, agreement_index, agreement_contracts_ids, items_ids,
                             data_path, tender_token):
    for agreement_contract_index, agreement_contract_id in enumerate(agreement_contracts_ids):
        data_file = 'agreement_{}_contracts_patch_{}.json'.format(agreement_index, agreement_contract_index)
        with ignore(IOError), open_file(get_data_file_path(data_file, data_path)) as f:
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


def wait_tender_awarded(client, tender_id):
    while True:
        response = client.get_tender(tender_id)
        if not response.json()['data']['status'] == 'active.awarded':
            sleep(TENDER_SECONDS_BUFFER)
        else:
            response_handler(response, tender_check_status_success_print_handler)
            break
    return response


def patch_tender_qual(client, data_path, tender_id, tender_token):
    with ignore(IOError), open_file(get_data_file_path('tender_patch_qual.json', data_path)) as f:
        tender_patch_data = json.loads(f.read())
        return client.patch_tender(tender_id, tender_token, tender_patch_data,
                                   success_handler=tender_patch_status_success_print_handler)


def patch_awards(client, tender_id, awards_ids, data_path, tender_token):
    for award_index, awards_id in enumerate(awards_ids):
        data_file = 'award_patch_{}.json'.format(award_index)
        with ignore(IOError), open_file(get_data_file_path(data_file, data_path)) as f:
            award_patch_data = json.loads(f.read())
            client.patch_award(tender_id, awards_id, tender_token, award_patch_data,
                               success_handler=item_patch_success_print_handler)


def get_awards(client, tender_id):
    while True:
        response = client.get_awards(tender_id)
        if not response.json()['data']:
            sleep(TENDER_SECONDS_BUFFER)
        else:
            response_handler(response, item_get_success_print_handler)
            break
    return response


def wait_tender_auction(client, tender_id):
    while True:
        response = client.get_tender(tender_id)
        if not response.json()['data']['status'] == 'active.auction':
            sleep(TENDER_SECONDS_BUFFER)
        else:
            response_handler(response, tender_check_status_success_print_handler)
            break
    return response


def patch_tender_pre(client, data_path, tender_id, tender_token):
    with ignore(IOError), open_file(get_data_file_path('tender_patch_pre.json', data_path)) as f:
        tender_patch_data = json.loads(f.read())
        return client.patch_tender(tender_id, tender_token, tender_patch_data,
                                   success_handler=tender_patch_status_success_print_handler)


def patch_qualifications(client, data_path, tender_id, qualifications_ids, tender_token):
    for qualification_index, qualification_id in enumerate(qualifications_ids):
        data_file = 'qualification_patch_{}.json'.format(qualification_index)
        with ignore(IOError), open_file(get_data_file_path(data_file, data_path)) as f:
            qualification_patch_data = json.loads(f.read())
            client.patch_qualification(tender_id, qualification_id, tender_token, qualification_patch_data,
                                       success_handler=item_patch_success_print_handler)


def get_qualifications(client, tender_id):
    while True:
        response = client.get_qualifications(tender_id)
        if not response.json()['data']:
            sleep(TENDER_SECONDS_BUFFER)
        else:
            response_handler(response, item_get_success_print_handler)
            break
    return response


def create_bids(client, data_path, data_files, tender_id):
    bid_files = []
    for data_file in data_files:
        if data_file.startswith('bid_create'):
            bid_files.append(data_file)
    for bid_file in bid_files:
        with ignore(IOError), open_file(get_data_file_path(bid_file, data_path)) as f:
            bid_create_data = json.loads(f.read())
            client.post_bid(tender_id, bid_create_data, success_handler=bid_create_success_print_handler)


def create_tender(client, data_path, acceleration):
    with ignore(IOError, handler=lambda: exit(0)), open_file(get_data_file_path('tender_create.json', data_path)) as f:
        tender_create_data = json.loads(f.read())
        set_acceleration_data(tender_create_data, acceleration=acceleration)
        response = client.post_tender(tender_create_data, success_handler=tender_create_success_print_handler)
        return response


def create_procedure(host, token, path, data, acceleration):
    data_path = get_data_path(data)
    data_files = get_data_all_files(data_path)

    client = TendersApiClient(host, token, path)

    print("Creating tender...\n")
    response = create_tender(client, data_path, acceleration)
    tender_id = get_tender_id(response)
    tender_token = get_tender_token(response)
    tender_period_seconds = get_tender_period_seconds(response)

    method_type = response.json()['data']['procurementMethodType']

    if method_type in (
        'closeFrameworkAgreementUA',
        'aboveThresholdUA',
    ):
        print("Creating bids...\n")
        create_bids(client, data_path, data_files, tender_id)

    if method_type in (
        'closeFrameworkAgreementUA',
        'aboveThresholdUA',
    ):
        print("Waiting {} seconds for end of tender period...\n".format(tender_period_seconds))
        sleep(tender_period_seconds + TENDER_SECONDS_BUFFER)

    if method_type in (
        'closeFrameworkAgreementUA',
    ):
        print("Checking qualifications...\n")
        response = get_qualifications(client, tender_id)
        qualifications_ids = [i['id'] for i in response.json()['data']]
        print("Patching qualifications...\n")
        patch_qualifications(client, data_path, tender_id, qualifications_ids, tender_token)

    if method_type in (
        'closeFrameworkAgreementUA',
    ):
        print("Approving qualifications by switching to next status...\n")
        response = patch_tender_pre(client, data_path, tender_id, tender_token)
        qualification_period_seconds = get_qualification_period_seconds(response)
        print("Waiting {} seconds for end of qualification period...\n".format(qualification_period_seconds))
        sleep(qualification_period_seconds + TENDER_SECONDS_BUFFER)

    if method_type in (
        'closeFrameworkAgreementUA',
        'aboveThresholdUA',
    ):
        print("Waiting for active.auction...\n")
        wait_tender_auction(client, tender_id)

    if method_type in (
        'closeFrameworkAgreementUA',
        'aboveThresholdUA',
    ):
        print("Checking awards...\n")
        response = get_awards(client, tender_id)
        awards_ids = [i['id'] for i in response.json()['data']]
        print("Patching awards...\n")
        patch_awards(client, tender_id, awards_ids, data_path, tender_token)

    if method_type in (
        'closeFrameworkAgreementUA',
    ):
        print("Approving awards by switching to next status...\n")
        patch_tender_qual(client, data_path, tender_id, tender_token)

    if method_type in (
        'closeFrameworkAgreementUA',
    ):
        print("Waiting for active.awarded...\n")
        wait_tender_awarded(client, tender_id)

    if method_type in (
        'aboveThresholdUA',
    ):
        print("Completing tender by switching to next status...\n")
        patch_tender_awarded(client, data_path, tender_id, tender_token)

    if method_type in (
        'closeFrameworkAgreementUA',
    ):
        print("Checking agreements...\n")
        patch_agreements_with_contracts(client, tender_id, data_path, tender_token)

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
    args = parser.parse_args()

    create_procedure(args.host, args.token, args.path, args.data, args.acceleration)


if __name__ == "__main__":
    main()
