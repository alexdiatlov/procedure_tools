from __future__ import absolute_import

import logging
import random

from faker import Faker

from procedure_tools.utils.process import (
    get_tender,
    patch_tender_qual,
    patch_tender_waiting,
    patch_awards,
    get_awards,
    patch_contracts,
    get_contracts,
    patch_tender_pre,
    patch_qualifications,
    get_qualifications,
    create_awards,
    create_bids,
    create_tender,
    patch_tender,
    wait,
    wait_status,
    patch_stage2_credentials,
    patch_tender_tendering,
    patch_tender_pending,
    wait_edr_pre_qual,
    wait_edr_qual,
    get_agreement,
    get_contract,
    patch_contract_credentials,
    wait_auction_participation_urls,
    post_criteria,
    patch_bids,
    post_bid_res,
    create_plans,
    post_tender_plan,
    create_plan,
    patch_plan,
    get_agreements,
    patch_agreements_contracts,
    patch_agreements,
    upload_tender_documents,
    patch_contract_unit_values,
    extend_tender_period,
    create_complaints,
    patch_complaints,
)
from procedure_tools.client import (
    TendersApiClient,
    AgreementsApiClient,
    ContractsApiClient,
    PlansApiClient,
    DsApiClient,
)
from procedure_tools.utils.data import (
    get_id,
    get_token,
    get_procurement_method_type,
    get_submission_method_details,
    get_next_check,
    get_complaint_period_end_dates,
    get_ids,
    get_tender_period,
    get_procurement_entity_kind,
    get_contract_period_clarif_date,
    get_config,
    get_contracts_items_ids,
    TENDER_PERIOD_MIN_TIMEDELTA,
    TENDER_PERIOD_MIN_BELOW_TIMEDELTA,
)
from procedure_tools.utils.file import get_data_path

try:
    from colorama import init

    init()
except ImportError:
    pass

WAIT_EDR_QUAL = "edr-qualification"
WAIT_EDR_PRE_QUAL = "edr-pre-qualification"


def set_faker_seed(args):
    faker_seed = args.seed or random.randint(0, 1000000)
    logging.info(f"Using seed {faker_seed}\n")
    Faker.seed(faker_seed)


def init_procedure(args, session=None):
    set_faker_seed(args)

    data_path = get_data_path(args.data)
    if data_path is None:
        logging.error("Data path not found.\n")
    else:
        process_procedure(args, session=session)
        logging.info("Completed.\n")


def process_procedure(
    args,
    tender_id=None,
    tender_token=None,
    filename_prefix="",
    session=None,
):
    tenders_client = TendersApiClient(
        args.host,
        args.token,
        args.path,
        session=session,
        debug=args.debug,
    )
    tenders_reviewer_client = (
        TendersApiClient(
            args.host,
            args.reviewer_token,
            args.path,
            session=session,
            debug=args.debug,
        )
        if args.reviewer_token
        else None
    )
    tenders_bot_client = (
        TendersApiClient(
            args.host,
            args.bot_token,
            args.path,
            session=session,
            debug=args.debug,
        )
        if args.bot_token
        else None
    )
    plans_client = PlansApiClient(
        args.host,
        args.token,
        args.path,
        session=session,
        debug=args.debug,
    )
    ds_client = DsApiClient(
        args.ds_host,
        args.ds_username,
        args.ds_password,
        session=session,
        debug=args.debug,
    )

    if not tender_id and not tender_token:
        response = create_plan(plans_client, args)

        if response:
            plan_id = get_id(response)
            plan_token = get_token(response)
            response = patch_plan(
                plans_client,
                args,
                plan_id,
                plan_token,
            )
            response = create_tender(
                plans_client,
                ds_client,
                args,
                plan_id=plan_id,
            )
        else:
            plan_id = None
            response = create_tender(
                tenders_client,
                ds_client,
                args,
            )

        if not response:
            return

        tender_id = get_id(response)
        tender_token = get_token(response)

        if not plan_id:
            plans_responses = create_plans(plans_client, args)
            for plan_response in plans_responses:
                plan_id = plan_response.json()["data"]["id"]
                post_tender_plan(
                    tenders_client,
                    args,
                    tender_id,
                    tender_token,
                    plan_id,
                )

    response = get_tender(tenders_client, args, tender_id)
    config = get_config(response)

    method_type = get_procurement_method_type(response)
    submission_method_details = get_submission_method_details(response)
    procurement_entity_kind = get_procurement_entity_kind(response)

    upload_tender_documents(
        tenders_client,
        ds_client,
        args,
        tender_id,
        tender_token,
        filename_prefix=filename_prefix,
    )

    if method_type in (
        "belowThreshold",
        "aboveThreshold",
        "aboveThresholdUA",
        "aboveThresholdEU",
        "closeFrameworkAgreementUA",
        "competitiveDialogueEU",
        "competitiveDialogueUA",
        "competitiveDialogueEU.stage2",
        "competitiveDialogueUA.stage2",
        "esco",
    ):
        criteria_response = post_criteria(
            tenders_client,
            args,
            tender_id,
            tender_token,
            filename_prefix=filename_prefix,
        )
        if criteria_response:
            tender_criteria = criteria_response.json()["data"]
        else:
            tender_criteria = None
    else:
        tender_criteria = None

    if method_type in (
        "belowThreshold",
        "aboveThreshold",
        "aboveThresholdUA",
        "aboveThresholdEU",
        "aboveThresholdUA.defense",
        "closeFrameworkAgreementUA",
        "competitiveDialogueEU",
        "competitiveDialogueUA",
        "negotiation",
        "negotiation.quick",
        "reporting",
        "esco",
        "simple.defense",
    ):
        response = patch_tender(
            tenders_client,
            args,
            tender_id,
            tender_token,
            filename_prefix=filename_prefix,
        )

    if method_type in ("closeFrameworkAgreementSelectionUA",):
        patch_tender_pending(
            tenders_client,
            args,
            tender_id,
            tender_token,
            filename_prefix=filename_prefix,
        )

    if method_type in ("closeFrameworkAgreementSelectionUA",):
        wait_status(tenders_client, args, tender_id, "active.enquiries")

    if method_type in ("belowThreshold",):
        wait(
            get_next_check(response),
            client_timedelta=tenders_client.client_timedelta,
            date_info_str="next chronograph check",
        )

    if method_type in ("belowThreshold", "closeFrameworkAgreementSelectionUA"):
        response = get_tender(tenders_client, args, tender_id)

        def fallback():
            """
            We need to extend tender period
            so that we don't switch to active.tendering
            after tenderPeriod.endDate
            :return:
            """
            extend_tender_period(
                tender_period=get_tender_period(response),
                client=tenders_client,
                args=args,
                tender_id=tender_id,
                tender_token=tender_token,
                period_timedelta=TENDER_PERIOD_MIN_BELOW_TIMEDELTA,
            )

        wait_status(
            tenders_client,
            args,
            tender_id,
            "active.tendering",
            delay=TENDER_PERIOD_MIN_BELOW_TIMEDELTA.seconds * 0.9,
            fallback=fallback,
        )

    if method_type in ("competitiveDialogueEU.stage2", "competitiveDialogueUA.stage2"):
        response = get_tender(tenders_client, args, tender_id)
        extend_tender_period(
            tender_period=get_tender_period(response),
            client=tenders_client,
            args=args,
            tender_id=tender_id,
            tender_token=tender_token,
            period_timedelta=TENDER_PERIOD_MIN_TIMEDELTA,
        )

    if method_type in ("competitiveDialogueEU.stage2", "competitiveDialogueUA.stage2"):
        patch_tender_tendering(
            tenders_client,
            args,
            tender_id,
            tender_token,
            filename_prefix=filename_prefix,
        )

    comp_responses = create_complaints(
        tenders_client,
        args,
        tender_id,
        tender_token,
        file_subpath="complaints",
        filename_prefix=filename_prefix,
    )
    if comp_responses:
        comp_jsons = [comp_response.json() for comp_response in comp_responses]
        comp_ids = [comp_json["data"]["id"] for comp_json in comp_jsons]
        comp_tokens = [comp_json["access"]["token"] for comp_json in comp_jsons]
        patch_complaints(
            tenders_client,
            tenders_bot_client,
            tenders_reviewer_client,
            args,
            tender_id,
            tender_token,
            comp_ids,
            comp_tokens,
            file_subpath="complaints",
            filename_prefix=filename_prefix,
        )

    bids_tokens = []

    if method_type in (
        "belowThreshold",
        "aboveThreshold",
        "aboveThresholdUA",
        "aboveThresholdEU",
        "closeFrameworkAgreementUA",
        "closeFrameworkAgreementSelectionUA",
        "aboveThresholdUA.defense",
        "competitiveDialogueEU",
        "competitiveDialogueUA",
        "competitiveDialogueEU.stage2",
        "competitiveDialogueUA.stage2",
        "esco",
        "simple.defense",
    ):
        bids_responses = create_bids(
            tenders_client,
            ds_client,
            args,
            tender_id,
            filename_prefix=filename_prefix,
        )
        bids_jsons = [bids_response.json() for bids_response in bids_responses]
        bids_ids = [bid_json["data"]["id"] for bid_json in bids_jsons]
        bids_tokens = [bid_json["access"]["token"] for bid_json in bids_jsons]
        if tender_criteria:
            bids_documents = [bid_json["data"]["documents"] for bid_json in bids_jsons]
            post_bid_res(
                tenders_client,
                args,
                tender_id,
                bids_ids,
                bids_tokens,
                bids_documents,
                tender_criteria,
                filename_prefix=filename_prefix,
            )
        patch_bids(
            tenders_client,
            args,
            tender_id,
            bids_ids,
            bids_tokens,
            filename_prefix=filename_prefix,
        )
    else:
        bids_jsons = None

    if method_type in (
        "belowThreshold",
        "aboveThreshold",
        "aboveThresholdUA",
        "aboveThresholdEU",
        "closeFrameworkAgreementUA",
        "closeFrameworkAgreementSelectionUA",
        "aboveThresholdUA.defense",
        "competitiveDialogueEU",
        "competitiveDialogueUA",
        "competitiveDialogueEU.stage2",
        "competitiveDialogueUA.stage2",
        "esco",
        "simple.defense",
    ):
        response = get_tender(tenders_client, args, tender_id)
        wait(
            get_next_check(response),
            client_timedelta=tenders_client.client_timedelta,
            date_info_str="next chronograph check",
        )

    if WAIT_EDR_PRE_QUAL in args.wait.split(","):
        wait_edr_pre_qual(tenders_client, args, tender_id)

    qualifications_ids = []

    if config.get("hasPrequalification", False):
        response = get_qualifications(tenders_client, args, tender_id)
        qualifications_ids = get_ids(response)
        patch_qualifications(
            tenders_client,
            args,
            tender_id,
            qualifications_ids,
            tender_token,
            filename_prefix=filename_prefix,
        )

        patch_tender_pre(
            tenders_client,
            args,
            tender_id,
            tender_token,
            filename_prefix=filename_prefix,
        )

    if bids_tokens:
        for qualification_index, qualification_id in enumerate(qualifications_ids):
            comp_responses = create_complaints(
                tenders_client,
                args,
                tender_id,
                bids_tokens[0],  # any of suppliers can create complaint
                obj_type="qualification",
                obj_index=qualification_index,
                obj_id=qualification_id,
                file_subpath="qualifications_complaints",
                filename_prefix=filename_prefix,
            )
            if comp_responses:
                comp_jsons = [comp_response.json() for comp_response in comp_responses]
                comp_ids = [comp_json["data"]["id"] for comp_json in comp_jsons]
                comp_tokens = [comp_json["access"]["token"] for comp_json in comp_jsons]
                patch_complaints(
                    tenders_client,
                    tenders_bot_client,
                    tenders_reviewer_client,
                    args,
                    tender_id,
                    tender_token,
                    comp_ids,
                    comp_tokens,
                    obj_type="qualification",
                    obj_index=qualification_index,
                    obj_id=qualification_id,
                    file_subpath="qualifications_complaints",
                    filename_prefix=filename_prefix,
                )

    response = get_tender(tenders_client, args, tender_id)
    tender_status = response.json()["data"]["status"]

    if tender_status == "active.pre-qualification":
        # satisfied complaint changes tender status to active.pre-qualification,
        # so we need to switch it again to active.pre-qualification.stand-still
        patch_tender_pre(
            tenders_client,
            args,
            tender_id,
            tender_token,
            filename_prefix=filename_prefix,
        )

    if method_type in ("competitiveDialogueEU", "competitiveDialogueUA"):
        wait_status(tenders_client, args, tender_id, "active.stage2.pending")
        patch_tender_waiting(tenders_client, args, tender_id, tender_token)

    if method_type in (
        "closeFrameworkAgreementUA",
        "closeFrameworkAgreementSelectionUA",
        "aboveThresholdUA.defense",
        "aboveThresholdEU",
        "belowThreshold",
        "competitiveDialogueEU.stage2",
        "esco",
        "simple.defense",
    ):
        wait_status(
            tenders_client,
            args,
            tender_id,
            ["active.auction", "active.qualification", "active.awarded"],
        )

    if (
        config.get("hasAuction")
        and bids_jsons
        and (
            not submission_method_details
            or all(
                [
                    "mode:fast-forward" not in submission_method_details,
                    "mode:no-auction" not in submission_method_details,
                ]
            )
        )
    ):
        wait_auction_participation_urls(tenders_client, tender_id, bids_jsons)

    if method_type in ("negotiation", "negotiation.quick", "reporting"):
        create_awards(tenders_client, args, tender_id, tender_token)

    if method_type in ("negotiation", "negotiation.quick", "reporting"):
        wait_status(tenders_client, args, tender_id, "active")

    if WAIT_EDR_QUAL in args.wait.split(","):
        wait_edr_qual(tenders_client, args, tender_id)

    awards_ids = []

    if method_type in (
        "belowThreshold",
        "aboveThreshold",
        "aboveThresholdUA",
        "aboveThresholdEU",
        "closeFrameworkAgreementUA",
        "closeFrameworkAgreementSelectionUA",
        "aboveThresholdUA.defense",
        "competitiveDialogueEU.stage2",
        "competitiveDialogueUA.stage2",
        "negotiation",
        "negotiation.quick",
        "reporting",
        "esco",
        "simple.defense",
    ):
        response = get_awards(tenders_client, args, tender_id)
        awards_ids = get_ids(response)
        patch_awards(
            tenders_client,
            args,
            tender_id,
            awards_ids,
            tender_token,
            filename_prefix=filename_prefix,
        )

    if method_type in ("closeFrameworkAgreementUA",):
        patch_tender_qual(tenders_client, args, tender_id, tender_token)

    if bids_tokens:
        for award_index, award_id in enumerate(awards_ids):
            comp_responses = create_complaints(
                tenders_client,
                args,
                tender_id,
                bids_tokens[0],  # any of suppliers can create complaint
                obj_type="award",
                obj_index=award_index,
                obj_id=award_id,
                file_subpath="awards_complaints",
                filename_prefix=filename_prefix,
            )
            if comp_responses:
                comp_jsons = [comp_response.json() for comp_response in comp_responses]
                comp_ids = [comp_json["data"]["id"] for comp_json in comp_jsons]
                comp_tokens = [comp_json["access"]["token"] for comp_json in comp_jsons]
                patch_complaints(
                    tenders_client,
                    tenders_bot_client,
                    tenders_reviewer_client,
                    args,
                    tender_id,
                    tender_token,
                    comp_ids,
                    comp_tokens,
                    obj_type="award",
                    obj_index=award_index,
                    obj_id=award_id,
                    file_subpath="awards_complaints",
                    filename_prefix=filename_prefix,
                )

    if method_type in ("closeFrameworkAgreementUA",):
        response = get_tender(tenders_client, args, tender_id)
        tender_status = response.json()["data"]["status"]

        if tender_status == "active.qualification":
            # satisfied complaint changes tender status to active.qualification,
            # so we need to switch it again to active.qualification.stand-still
            patch_tender_qual(tenders_client, args, tender_id, tender_token)

    if method_type in (
        "closeFrameworkAgreementUA",
        "aboveThresholdEU",
        "competitiveDialogueEU.stage2",
        "esco",
    ):
        wait_status(tenders_client, args, tender_id, "active.awarded")

    if method_type in (
        "belowThreshold",
        "aboveThreshold",
        "aboveThresholdUA",
        "aboveThresholdEU",
        "aboveThresholdUA.defense",
        "competitiveDialogueEU.stage2",
        "competitiveDialogueUA.stage2",
        "negotiation",
        "negotiation.quick",
        "esco",
        "simple.defense",
    ):
        response = get_awards(tenders_client, args, tender_id)
        awards_complaint_dates = get_complaint_period_end_dates(response)
        wait(
            max(awards_complaint_dates),
            client_timedelta=tenders_client.client_timedelta,
            date_info_str="end of award complaint period",
        )

    contracts_ids = []
    items_ids = []

    if method_type in (
        "belowThreshold",
        "aboveThreshold",
        "aboveThresholdUA",
        "aboveThresholdEU",
        "closeFrameworkAgreementSelectionUA",
        "aboveThresholdUA.defense",
        "competitiveDialogueEU.stage2",
        "competitiveDialogueUA.stage2",
        "negotiation",
        "negotiation.quick",
        "reporting",
        "esco",
        "simple.defense",
    ):
        response = get_contracts(tenders_client, args, tender_id)
        contracts_ids = get_ids(response)
        items_ids = get_contracts_items_ids(response)

    if method_type in (
        "belowThreshold",
        "aboveThreshold",
        "aboveThresholdUA",
        "aboveThresholdEU",
        "closeFrameworkAgreementSelectionUA",
        "aboveThresholdUA.defense",
        "competitiveDialogueEU.stage2",
        "competitiveDialogueUA.stage2",
        "negotiation",
        "negotiation.quick",
        "reporting",
        "simple.defense",
    ):
        patch_contract_unit_values(
            tenders_client,
            args,
            tender_id,
            contracts_ids,
            items_ids,
            tender_token,
            filename_prefix=filename_prefix,
        )

    if method_type in (
        "belowThreshold",
        "aboveThreshold",
        "aboveThresholdUA",
        "aboveThresholdEU",
        "closeFrameworkAgreementSelectionUA",
        "aboveThresholdUA.defense",
        "competitiveDialogueEU.stage2",
        "competitiveDialogueUA.stage2",
        "negotiation",
        "negotiation.quick",
        "reporting",
        "esco",
        "simple.defense",
    ):
        patch_contracts(
            tenders_client,
            args,
            tender_id,
            contracts_ids,
            tender_token,
            filename_prefix=filename_prefix,
        )

    if method_type in (
        "belowThreshold",
        "aboveThreshold",
        "aboveThresholdUA",
        "aboveThresholdEU",
        "closeFrameworkAgreementSelectionUA",
        "aboveThresholdUA.defense",
        "competitiveDialogueEU.stage2",
        "competitiveDialogueUA.stage2",
        "negotiation",
        "negotiation.quick",
        "reporting",
        "simple.defense",
    ):
        for contracts_id in contracts_ids:
            contracts_client = ContractsApiClient(
                args.host,
                args.token,
                args.path,
                session=session,
                debug=args.debug,
            )
            get_contract(contracts_client, args, contracts_id)
            patch_contract_credentials(
                contracts_client,
                args,
                contracts_id,
                tender_token,
            )

    if method_type in ("closeFrameworkAgreementUA",):
        response = get_tender(tenders_client, args, tender_id)
        contract_period_clarif_date = get_contract_period_clarif_date(response)
        wait(
            contract_period_clarif_date,
            client_timedelta=tenders_client.client_timedelta,
            date_info_str="contract period clarifications until date",
        )
        response = get_agreements(tenders_client, args, tender_id)
        agreements_ids = get_ids(response)
        patch_agreements_contracts(
            tenders_client,
            args,
            tender_id,
            agreements_ids,
            tender_token,
        )
        patch_agreements(
            tenders_client,
            ds_client,
            args,
            tender_id,
            agreements_ids,
            tender_token,
        )

    if method_type in (
        "belowThreshold",
        "aboveThreshold",
        "aboveThresholdUA",
        "aboveThresholdEU",
        "closeFrameworkAgreementUA",
        "aboveThresholdUA.defense",
        "competitiveDialogueEU",
        "competitiveDialogueUA",
        "competitiveDialogueEU.stage2",
        "competitiveDialogueUA.stage2",
        "negotiation",
        "negotiation.quick",
        "reporting",
        "esco",
        "simple.defense",
    ):
        wait_status(tenders_client, args, tender_id, "complete")

    if method_type in (
        "competitiveDialogueEU",
        "competitiveDialogueUA",
    ):
        response = get_tender(tenders_client, args, tender_id)
        tender_id = response.json()["data"]["stage2TenderID"]
        response = patch_stage2_credentials(
            tenders_client,
            args,
            tender_id,
            tender_token,
        )
        tender_token = get_token(response)

        process_procedure(
            args,
            tender_id=tender_id,
            tender_token=tender_token,
            filename_prefix="stage2_",
            session=session,
        )

    if method_type in ("closeFrameworkAgreementUA",):
        response = get_tender(tenders_client, args, tender_id)
        agreement_id = response.json()["data"]["agreements"][-1]["id"]

        agreement_client = AgreementsApiClient(
            args.host,
            args.token,
            args.path,
            session=session,
            debug=args.debug,
        )
        get_agreement(agreement_client, args, agreement_id)

        response = create_tender(
            tenders_client,
            ds_client,
            args,
            agreement_id=agreement_id,
            filename_prefix="selection_",
        )
        tender_id = get_id(response)
        tender_token = get_token(response)

        process_procedure(
            args,
            tender_id=tender_id,
            tender_token=tender_token,
            filename_prefix="selection_",
            session=session,
        )
