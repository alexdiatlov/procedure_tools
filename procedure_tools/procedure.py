from __future__ import absolute_import

import logging

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
    extend_tender_period_min,
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
    get_agreements,
    patch_agreements_contracts,
    patch_agreements,
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
)

try:
    from colorama import init

    init()
except ImportError:
    pass

WAIT_EDR_QUAL = "edr-qualification"
WAIT_EDR_PRE_QUAL = "edr-pre-qualification"


def init_procedure(args, session=None):
    process_procedure(args, session=session)
    logging.info("Completed.\n")


def process_procedure(
    args,
    tender_id=None,
    tender_token=None,
    filename_prefix="",
    session=None,
):
    tenders_client = TendersApiClient(args.host, args.token, args.path, session=session)
    plans_client = PlansApiClient(args.host, args.token, args.path, session=session)

    if not tender_id and not tender_token:
        response = create_plan(plans_client, args)

        if response:
            plan_id = get_id(response)
            response = create_tender(plans_client, args, plan_id=plan_id)
        else:
            plan_id = None
            response = create_tender(tenders_client, args)

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
    method_type = get_procurement_method_type(response)
    submission_method_details = get_submission_method_details(response)
    procurement_entity_kind = get_procurement_entity_kind(response)

    if method_type in (
        "aboveThresholdEU",
        "aboveThresholdUA",
        "belowThreshold",
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
        "aboveThresholdEU",
        "aboveThresholdUA",
        "aboveThresholdUA.defense",
        "belowThreshold",
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
            extend_tender_period_min(
                get_tender_period(response),
                tenders_client,
                args,
                tender_id,
                tender_token,
            )

        wait_status(
            tenders_client,
            args,
            tender_id,
            "active.tendering",
            fallback=fallback,
        )

    if method_type in ("competitiveDialogueEU.stage2", "competitiveDialogueUA.stage2"):
        response = get_tender(tenders_client, args, tender_id)
        extend_tender_period_min(
            get_tender_period(response),
            tenders_client,
            args,
            tender_id,
            tender_token,
        )

    if method_type in ("competitiveDialogueEU.stage2", "competitiveDialogueUA.stage2"):
        patch_tender_tendering(
            tenders_client,
            args,
            tender_id,
            tender_token,
            filename_prefix=filename_prefix,
        )

    if method_type in (
        "closeFrameworkAgreementUA",
        "closeFrameworkAgreementSelectionUA",
        "aboveThresholdUA",
        "aboveThresholdUA.defense",
        "aboveThresholdEU",
        "belowThreshold",
        "competitiveDialogueEU",
        "competitiveDialogueUA",
        "competitiveDialogueEU.stage2",
        "competitiveDialogueUA.stage2",
        "esco",
        "simple.defense",
    ):
        ds_client = DsApiClient(
            args.ds_host,
            args.ds_username,
            args.ds_password,
            session=session,
        )
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
        bids_responses = None

    if method_type in (
        "closeFrameworkAgreementUA",
        "closeFrameworkAgreementSelectionUA",
        "aboveThresholdUA",
        "aboveThresholdUA.defense",
        "aboveThresholdEU",
        "belowThreshold",
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

    if method_type in (
        "closeFrameworkAgreementUA",
        "aboveThresholdEU",
        "competitiveDialogueEU",
        "competitiveDialogueUA",
        "competitiveDialogueEU.stage2",
        "esco",
    ):
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

    if method_type in (
        "closeFrameworkAgreementUA",
        "aboveThresholdEU",
        "competitiveDialogueEU",
        "competitiveDialogueUA",
        "competitiveDialogueEU.stage2",
        "esco",
    ):
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
        method_type
        in (
            "closeFrameworkAgreementUA",
            "closeFrameworkAgreementSelectionUA",
            "aboveThresholdUA",
            "aboveThresholdUA.defense",
            "aboveThresholdEU",
            "belowThreshold",
            "competitiveDialogueEU.stage2",
            "competitiveDialogueUA.stage2",
            "esco",
            "simple.defense",
        )
        and bids_responses
        and all(
            [
                "mode:fast-forward" not in submission_method_details,
                "mode:no-auction" not in submission_method_details,
            ]
        )
    ):
        wait_auction_participation_urls(tenders_client, tender_id, bids_responses)

    if method_type in ("negotiation", "negotiation.quick", "reporting"):
        create_awards(tenders_client, args, tender_id, tender_token)

    if method_type in ("negotiation", "negotiation.quick", "reporting"):
        wait_status(tenders_client, args, tender_id, "active")

    if WAIT_EDR_QUAL in args.wait.split(","):
        wait_edr_qual(tenders_client, args, tender_id)

    if method_type in (
        "closeFrameworkAgreementUA",
        "closeFrameworkAgreementSelectionUA",
        "aboveThresholdUA",
        "aboveThresholdUA.defense",
        "aboveThresholdEU",
        "belowThreshold",
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

    if method_type in (
        "closeFrameworkAgreementUA",
        "aboveThresholdEU",
        "competitiveDialogueEU.stage2",
        "esco",
    ):
        wait_status(tenders_client, args, tender_id, "active.awarded")

    if method_type in (
        "aboveThresholdUA",
        "aboveThresholdUA.defense",
        "aboveThresholdEU",
        "belowThreshold",
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

    if method_type in (
        "closeFrameworkAgreementSelectionUA",
        "aboveThresholdUA",
        "aboveThresholdUA.defense",
        "aboveThresholdEU",
        "belowThreshold",
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
        patch_contracts(
            tenders_client,
            args,
            tender_id,
            contracts_ids,
            tender_token,
            filename_prefix=filename_prefix,
        )

    if method_type in (
        "closeFrameworkAgreementSelectionUA",
        "aboveThresholdUA",
        "aboveThresholdUA.defense",
        "aboveThresholdEU",
        "belowThreshold",
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
        patch_agreements_contracts(tenders_client, args, tender_id, agreements_ids, tender_token)
        patch_agreements(tenders_client, args, tender_id, agreements_ids, tender_token)

    if method_type in (
        "closeFrameworkAgreementUA",
        "aboveThresholdUA",
        "aboveThresholdUA.defense",
        "aboveThresholdEU",
        "belowThreshold",
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
        )
        get_agreement(agreement_client, args, agreement_id)

        response = create_tender(
            tenders_client,
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
