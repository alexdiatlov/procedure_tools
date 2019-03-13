import argparse
import sys

from procedure_tools.utils.data import get_complaint_period_end_date, get_ids
from procedure_tools.utils.process import (
    patch_agreements_with_contracts, get_tender, patch_tender_qual, patch_tender_waiting, patch_awards, get_awards,
    patch_contracts, get_contracts, patch_tender_pre, patch_qualifications, get_qualifications, create_awards,
    create_bids, create_tender, update_tender_period, wait, wait_status, patch_credentials, patch_tender_tendering,
    patch_tender_pending, wait_edr_pre_qual, wait_edr_qual)
from .version import __version__
from .client import TendersApiClient, API_PATH_PREFIX_DEFAULT
from .utils.file import get_default_data_dirs, DATA_DIR_DEFAULT
from .utils.data import (
    get_tender_id, get_tender_token, get_procurement_method_type, get_tender_next_check, ACCELERATION_DEFAULT)

WAIT_EDR_QUAL = 'edr-qualification'
WAIT_EDR_PRE_QUAL = 'edr-pre-qualification'

WAIT_EVENTS = (
    WAIT_EDR_QUAL,
    WAIT_EDR_PRE_QUAL,
)


def create_procedure(args):
    client = TendersApiClient(args.host, args.token, args.path)

    response = create_tender(client, args)
    tender_id = get_tender_id(response)
    tender_token = get_tender_token(response)

    process_procedure(client, args, tender_id, tender_token)

    print("Completed.\n")


def process_procedure(client, args, tender_id, tender_token, filename_prefix=''):
    response = get_tender(client, args, tender_id)
    method_type = get_procurement_method_type(response)

    if method_type in (
            'closeFrameworkAgreementSelectionUA',
    ):
        patch_tender_pending(client, args, tender_id, tender_token, filename_prefix)

    if method_type in (
            'closeFrameworkAgreementSelectionUA',
    ):
        wait_status(client, args, tender_id, 'active.enquiries')

    if method_type in (
            'belowThreshold',
    ):
        wait(get_tender_next_check(response), date_info_str='next chronograph check')

    if method_type in (
            'belowThreshold',
            'closeFrameworkAgreementSelectionUA',
    ):
        def update_tender_period_fallback():
            update_tender_period(client, args, tender_id, tender_token, args.acceleration)

        wait_status(client, args, tender_id, 'active.tendering', fallback=update_tender_period_fallback)

    if method_type in (
            'competitiveDialogueEU.stage2',
            'competitiveDialogueUA.stage2',
    ):
        update_tender_period(client, args, tender_id, tender_token, args.acceleration)

    if method_type in (
            'competitiveDialogueEU.stage2',
            'competitiveDialogueUA.stage2',
    ):
        patch_tender_tendering(client, args, tender_id, tender_token, filename_prefix)

    if method_type in (
            'closeFrameworkAgreementUA',
            'closeFrameworkAgreementSelectionUA',
            'aboveThresholdUA',
            'aboveThresholdUA.defense',
            'aboveThresholdEU',
            'belowThreshold',
            'competitiveDialogueEU',
            'competitiveDialogueUA',
            'competitiveDialogueEU.stage2',
            'competitiveDialogueUA.stage2',
            'esco',
    ):
        create_bids(client, args, tender_id, filename_prefix)

    if method_type in (
            'closeFrameworkAgreementUA',
            'closeFrameworkAgreementSelectionUA',
            'aboveThresholdUA',
            'aboveThresholdUA.defense',
            'aboveThresholdEU',
            'belowThreshold',
            'competitiveDialogueEU',
            'competitiveDialogueUA',
            'competitiveDialogueEU.stage2',
            'competitiveDialogueUA.stage2',
            'esco',
    ):
        response = get_tender(client, args, tender_id)
        wait(get_tender_next_check(response), date_info_str='next chronograph check')

    if WAIT_EDR_PRE_QUAL in args.wait.split(','):
        wait_edr_pre_qual(client, args, tender_id)

    if method_type in (
            'closeFrameworkAgreementUA',
            'aboveThresholdEU',
            'competitiveDialogueEU',
            'competitiveDialogueUA',
            'competitiveDialogueEU.stage2',
            'esco',
    ):
        response = get_qualifications(client, args, tender_id)
        qualifications_ids = get_ids(response)
        patch_qualifications(client, args, tender_id, qualifications_ids, tender_token, filename_prefix)

    if method_type in (
            'closeFrameworkAgreementUA',
            'aboveThresholdEU',
            'competitiveDialogueEU',
            'competitiveDialogueUA',
            'competitiveDialogueEU.stage2',
            'esco',
    ):
        patch_tender_pre(client, args, tender_id, tender_token, filename_prefix)

    if method_type in (
            'competitiveDialogueEU',
            'competitiveDialogueUA',
    ):
        wait_status(client, args, tender_id, 'active.stage2.pending')
        patch_tender_waiting(client, args, tender_id, tender_token)

    if method_type in (
            'closeFrameworkAgreementUA',
            'closeFrameworkAgreementSelectionUA',
            'aboveThresholdUA.defense',
            'aboveThresholdEU',
            'belowThreshold',
            'competitiveDialogueEU.stage2',
            'esco',
    ):
        wait_status(client, args, tender_id, 'active.auction')

    if method_type in (
            'negotiation',
            'negotiation.quick',
            'reporting',
    ):
        create_awards(client, args, tender_id, tender_token)

    if method_type in (
            'negotiation',
            'negotiation.quick',
            'reporting',
    ):
        wait_status(client, args, tender_id, 'active')

    if WAIT_EDR_QUAL in args.wait.split(','):
        wait_edr_qual(client, args, tender_id)

    if method_type in (
            'closeFrameworkAgreementUA',
            'closeFrameworkAgreementSelectionUA',
            'aboveThresholdUA',
            'aboveThresholdUA.defense',
            'aboveThresholdEU',
            'belowThreshold',
            'competitiveDialogueEU.stage2',
            'competitiveDialogueUA.stage2',
            'negotiation',
            'negotiation.quick',
            'reporting',
            'esco',
    ):
        response = get_awards(client, args, tender_id)
        awards_ids = get_ids(response)
        patch_awards(client, args, tender_id, awards_ids, tender_token, filename_prefix)

    if method_type in (
            'closeFrameworkAgreementUA',
    ):
        patch_tender_qual(client, args, tender_id, tender_token)

    if method_type in (
            'closeFrameworkAgreementUA',
            'aboveThresholdEU',
            'competitiveDialogueEU.stage2',
            'esco',
    ):
        wait_status(client, args, tender_id, 'active.awarded')

    if method_type in (
            'aboveThresholdUA',
            'aboveThresholdUA.defense',
            'aboveThresholdEU',
            'belowThreshold',
            'competitiveDialogueEU.stage2',
            'competitiveDialogueUA.stage2',
            'negotiation',
            'negotiation.quick',
            'esco',
    ):
        response = get_awards(client, args, tender_id)
        awards_complaint_dates = get_complaint_period_end_date(response)
        wait(max(awards_complaint_dates), date_info_str='end of award complaint period')

    if method_type in (
            'closeFrameworkAgreementSelectionUA',
            'aboveThresholdUA',
            'aboveThresholdUA.defense',
            'aboveThresholdEU',
            'belowThreshold',
            'competitiveDialogueEU.stage2',
            'competitiveDialogueUA.stage2',
            'negotiation',
            'negotiation.quick',
            'reporting',
            'esco',
    ):
        response = get_contracts(client, args, tender_id)
        contracts_ids = get_ids(response)
        patch_contracts(client, args, tender_id, contracts_ids, tender_token, filename_prefix)

    if method_type in (
            'closeFrameworkAgreementUA',
    ):
        patch_agreements_with_contracts(client, args, tender_id, tender_token)

    if method_type in (
            'closeFrameworkAgreementUA',
            'aboveThresholdUA',
            'aboveThresholdUA.defense',
            'aboveThresholdEU',
            'belowThreshold',
            'competitiveDialogueEU',
            'competitiveDialogueUA',
            'competitiveDialogueEU.stage2',
            'competitiveDialogueUA.stage2',
            'negotiation',
            'negotiation.quick',
            'reporting',
            'esco',
    ):
        wait_status(client, args, tender_id, 'complete')

    if method_type in (
            'competitiveDialogueEU',
            'competitiveDialogueUA',
    ):
        response = get_tender(client, args, tender_id)
        tender_id = response.json()['data']['stage2TenderID']
        response = patch_credentials(client, args, tender_id, tender_token)
        tender_token = get_tender_token(response)

        process_procedure(client, args, tender_id, tender_token, filename_prefix='stage2_')

    if method_type in (
            'closeFrameworkAgreementUA',
    ):
        response = get_tender(client, args, tender_id)
        agreement_id = response.json()['data']['agreements'][-1]['id']

        response = create_tender(client, args, agreement_id=agreement_id, filename_prefix='selection_')
        tender_id = get_tender_id(response)
        tender_token = get_tender_token(response)

        process_procedure(client, args, tender_id, tender_token, filename_prefix='selection_')


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
    parser.add_argument('-w', '--wait',
                        help='wait for event {} divided by comma)'.format(WAIT_EVENTS),
                        metavar=WAIT_EDR_QUAL,
                        default='')

    create_procedure(parser.parse_args())


if __name__ == "__main__":
    main()
