import json
import logging

import math

from datetime import timedelta
from mimetypes import MimeTypes
from time import sleep

from procedure_tools.utils.contextmanagers import (
    ignore,
    ignore_silent,
    open_file_or_exit,
    open_file,
)
from procedure_tools.utils.data import (
    TENDER_SECONDS_BUFFER,
    get_ids,
    get_items_ids,
    get_bids_ids,
    set_agreement_period,
    set_acceleration_data,
    set_tender_period_data,
    set_mode_data,
    DATETIME_MASK,
    TENDER_PERIOD_MIN_TIMEDELTA,
    TENDER_PERIOD_MAX_TIMEDELTA,
)
from procedure_tools.utils.date import (
    fix_datetime,
    get_utcnow,
    parse_date,
)
from procedure_tools.utils.file import (
    get_data_file_path,
    get_data_path,
    get_data_all_files,
)
from procedure_tools.utils.handlers import (
    item_patch_success_handler,
    tender_patch_success_handler,
    item_create_success_handler,
    bid_create_success_handler,
    tender_create_success_handler,
    response_handler,
    tender_check_status_success_handler,
    contract_credentials_success_handler,
    default_success_handler,
    plan_create_success_handler,
    plan_patch_success_handler,
    auction_participation_url_success_handler,
    tender_post_criteria_success_handler,
    tender_patch_period_success_handler,
    auction_multilot_participation_url_success_handler,
    tender_post_plan_success_handler,
)


EDR_FILENAME = "edr_identification.yaml"


def get_bids(client, args, tender_id):
    logging.info("Check bids...\n")
    while True:
        response = client.get_bids(tender_id)
        if not response.json()["data"]:
            sleep(TENDER_SECONDS_BUFFER)
        else:
            break
    return response


def patch_bids(client, args, tender_id, bids_ids, bids_tokens, filename_prefix=""):
    logging.info("Patching bids...\n")
    for bid_index, bid_id in enumerate(bids_ids):
        with ignore(IOError):
            data_file = "{}bid_patch_{}.json".format(filename_prefix, bid_index)
            path = get_data_file_path(data_file, get_data_path(args.data))
            with open_file_or_exit(path, exit_filename=args.stop) as f:
                bid_patch_data = json.loads(f.read())
                client.patch_bid(
                    tender_id,
                    bid_id,
                    bids_tokens[bid_index],
                    bid_patch_data,
                    success_handler=item_patch_success_handler,
                )


def post_bid_res(
    client,
    args,
    tender_id,
    bids_ids,
    bids_tokens,
    bids_documents,
    tender_criteria,
    filename_prefix="",
):
    logging.info("Post bids requirement responses...\n")
    for bid_index, bid_id in enumerate(bids_ids):
        with ignore(IOError):
            data_file = "{}bid_res_post_{}.json".format(filename_prefix, bid_index)
            path = get_data_file_path(data_file, get_data_path(args.data))
            with open_file_or_exit(path, exit_filename=args.stop) as f:
                bid_res_data = json.loads(f.read())
                for bid_res in bid_res_data["data"]:
                    if "evidences" in bid_res:
                        for evidence in bid_res["evidences"]:
                            if evidence["type"] == "document":
                                evidence["relatedDocument"]["id"] = bids_documents[
                                    bid_index
                                ][0]["id"]
                                evidence["relatedDocument"]["title"] = bids_documents[
                                    bid_index
                                ][0]["title"]
                    for tender_criteria_item in tender_criteria:
                        for group in tender_criteria_item["requirementGroups"]:
                            for req in group["requirements"]:
                                if bid_res["requirement"]["title"] == req["title"]:
                                    bid_res["requirement"]["id"] = req["id"]

                client.post_bid_res(
                    tender_id,
                    bid_id,
                    bids_tokens[bid_index],
                    bid_res_data,
                )


def patch_agreements_contracts(client, args, tender_id, agreements_ids, tender_token):
    response = get_tender(client, args, tender_id)
    items_ids = get_items_ids(response)
    response = get_bids(client, args, tender_id)
    bids_ids = get_ids(response)
    for agreement_index, agreement_id in enumerate(agreements_ids):
        response = get_agreement_contract(client, args, tender_id, agreement_id)
        agreement_contracts_ids = get_ids(response)
        agreement_contracts_related_bids = get_bids_ids(response)

        patch_agreement_contract(
            client,
            args,
            tender_id,
            agreement_id,
            agreement_index,
            agreement_contracts_ids,
            bids_ids,
            agreement_contracts_related_bids,
            items_ids,
            tender_token,
        )


def patch_agreement_contract(
    client,
    args,
    tender_id,
    agreement_id,
    agreement_index,
    agreement_contracts_ids,
    bids_ids,
    agreement_contracts_related_bids,
    items_ids,
    tender_token,
):
    logging.info("Patching agreement contracts...\n")
    for agreement_contract_index, agreement_contract_id in enumerate(
        agreement_contracts_ids
    ):
        with ignore(IOError):
            index = bids_ids.index(
                agreement_contracts_related_bids[agreement_contract_index]
            )
            data_file = "agreement_{}_contracts_patch_{}.json".format(
                agreement_index, index
            )
            path = get_data_file_path(data_file, get_data_path(args.data))
            with open_file_or_exit(path, exit_filename=args.stop) as f:
                agreement_contract_patch_data = json.loads(f.read())
                for item_index, items_id in enumerate(items_ids):
                    agreement_contract_patch_data["data"]["unitPrices"][item_index][
                        "relatedItem"
                    ] = items_id
                client.patch_agreement_contract(
                    tender_id,
                    agreement_id,
                    agreement_contract_id,
                    tender_token,
                    agreement_contract_patch_data,
                    success_handler=item_patch_success_handler,
                )


def patch_agreements(client, args, tender_id, agreements_ids, tender_token):
    logging.info("Patching agreements...\n")
    for agreement_index, agreement_id in enumerate(agreements_ids):
        with ignore(IOError):
            path = get_data_file_path(
                "agreement_patch_{}.json".format(agreement_index),
                get_data_path(args.data),
            )
            with open_file_or_exit(path, exit_filename=args.stop) as f:
                agreement_patch_data = json.loads(f.read())
                set_agreement_period(
                    agreement_patch_data["data"]["period"],
                    client_timedelta=client.client_timedelta,
                )
                client.patch_agreement(
                    tender_id,
                    agreement_id,
                    tender_token,
                    agreement_patch_data,
                    success_handler=item_patch_success_handler,
                )


def get_agreement_contract(client, args, tender_id, agreement_id):
    logging.info("Checking agreement contracts...")
    while True:
        response = client.get_agreement_contracts(tender_id, agreement_id)
        if not response.json()["data"]:
            sleep(TENDER_SECONDS_BUFFER)
        else:
            break
    return response


def get_tender(client, args, tender_id):
    return client.get_tender(tender_id)


def get_agreements(client, args, tender_id):
    logging.info("Check agreements...\n")
    while True:
        response = client.get_agreements(tender_id)
        if not response.json()["data"]:
            sleep(TENDER_SECONDS_BUFFER)
        else:
            break
    return response


def get_agreement(client, args, agreement_id):
    logging.info("Check agreement...\n")
    while True:
        response = client.get_agreement(
            agreement_id, error_handler=default_success_handler
        )
        if "data" not in response.json().keys():
            sleep(TENDER_SECONDS_BUFFER)
        else:
            break
    return response


def get_contract(client, args, contract_id):
    logging.info("Check contract...\n")
    while True:
        response = client.get_contract(
            contract_id, error_handler=default_success_handler
        )
        if "data" not in response.json().keys():
            sleep(TENDER_SECONDS_BUFFER)
        else:
            break
    return response


def patch_tender_qual(client, args, tender_id, tender_token):
    logging.info("Approving awards by switching to next status...\n")
    with ignore(IOError):
        path = get_data_file_path("tender_patch_qual.json", get_data_path(args.data))
        with open_file_or_exit(path, exit_filename=args.stop) as f:
            tender_patch_data = json.loads(f.read())
            return client.patch_tender(
                tender_id,
                tender_token,
                tender_patch_data,
                success_handler=tender_patch_success_handler,
            )


def patch_tender_waiting(client, args, tender_id, tender_token):
    logging.info("Finishing first stage by switching to next status...\n")
    with ignore(IOError):
        path = get_data_file_path("tender_patch_waiting.json", get_data_path(args.data))
        with open_file_or_exit(path, exit_filename=args.stop) as f:
            tender_patch_data = json.loads(f.read())
            return client.patch_tender(
                tender_id,
                tender_token,
                tender_patch_data,
                success_handler=tender_patch_success_handler,
            )


def patch_awards(client, args, tender_id, awards_ids, tender_token, filename_prefix=""):
    logging.info("Patching awards...\n")
    for award_index, awards_id in enumerate(awards_ids):
        with ignore(IOError):
            data_file = "{}award_patch_{}.json".format(filename_prefix, award_index)
            path = get_data_file_path(data_file, get_data_path(args.data))
            with open_file_or_exit(path, exit_filename=args.stop) as f:
                award_patch_data = json.loads(f.read())
                client.patch_award(
                    tender_id,
                    awards_id,
                    tender_token,
                    award_patch_data,
                    success_handler=item_patch_success_handler,
                )


def get_awards(client, args, tender_id):
    logging.info("Checking awards...\n")
    while True:
        response = client.get_awards(tender_id)
        if not response.json()["data"]:
            sleep(TENDER_SECONDS_BUFFER)
        else:
            break
    return response


def patch_contracts(
    client, args, tender_id, awards_ids, tender_token, filename_prefix=""
):
    logging.info("Patching contracts...\n")
    for contract_index, contract_id in enumerate(awards_ids):
        with ignore(IOError):
            data_file = "{}contract_patch_{}.json".format(
                filename_prefix, contract_index
            )
            path = get_data_file_path(data_file, get_data_path(args.data))
            with open_file_or_exit(path, exit_filename=args.stop) as f:
                contract_patch_data = json.loads(f.read())
                client.patch_contract(
                    tender_id,
                    contract_id,
                    tender_token,
                    contract_patch_data,
                    success_handler=item_patch_success_handler,
                )


def get_contracts(client, args, tender_id):
    logging.info("Checking contracts...\n")
    while True:
        response = client.get_contracts(tender_id)
        if not response.json()["data"]:
            sleep(TENDER_SECONDS_BUFFER)
        else:
            break
    return response


def patch_tender_pre(client, args, tender_id, tender_token, filename_prefix=""):
    logging.info("Approving qualifications by switching to next status...\n")
    with ignore(IOError):
        path = get_data_file_path(
            "{}tender_patch_pre.json".format(filename_prefix), get_data_path(args.data)
        )
        with open_file_or_exit(path, exit_filename=args.stop) as f:
            tender_patch_data = json.loads(f.read())
            return client.patch_tender(
                tender_id,
                tender_token,
                tender_patch_data,
                success_handler=tender_patch_success_handler,
            )


def patch_qualifications(
    client, args, tender_id, qualifications_ids, tender_token, filename_prefix=""
):
    logging.info("Patching qualifications...\n")
    for qualification_index, qualification_id in enumerate(qualifications_ids):
        with ignore(IOError):
            data_file = "{}qualification_patch_{}.json".format(
                filename_prefix, qualification_index
            )
            path = get_data_file_path(data_file, get_data_path(args.data))
            with open_file_or_exit(path, exit_filename=args.stop) as f:
                qualification_patch_data = json.loads(f.read())
                client.patch_qualification(
                    tender_id,
                    qualification_id,
                    tender_token,
                    qualification_patch_data,
                    success_handler=item_patch_success_handler,
                )


def get_qualifications(client, args, tender_id):
    logging.info("Checking qualifications...\n")
    while True:
        response = client.get_qualifications(tender_id)
        if not response.json()["data"]:
            sleep(TENDER_SECONDS_BUFFER)
        else:
            break
    return response


def create_awards(client, args, tender_id, tender_token):
    logging.info("Creating awards...\n")
    award_files = []
    for data_file in get_data_all_files(get_data_path(args.data)):
        if data_file.startswith("award_create"):
            award_files.append(data_file)
    for award_file in award_files:
        with ignore(IOError):
            path = get_data_file_path(award_file, get_data_path(args.data))
            with open_file_or_exit(path, exit_filename=args.stop) as f:
                award_create_data = json.loads(f.read())
                client.post_award(
                    tender_id,
                    tender_token,
                    award_create_data,
                    success_handler=item_create_success_handler,
                )


def create_bids(client, ds_client, args, tender_id, filename_prefix=""):
    logging.info("Creating bids...\n")
    bid_files = []
    for data_file in get_data_all_files(get_data_path(args.data)):
        if data_file.startswith("{}bid_create".format(filename_prefix)):
            bid_files.append(data_file)
    responses = []
    for bid_file in bid_files:
        bid_document_files = []
        bid_documents = []
        for data_file in get_data_all_files(get_data_path(args.data)):
            if data_file.startswith("{}bid_document".format(filename_prefix)):
                bid_document_files.append(data_file)
        for bid_document_file in bid_document_files:
            path = get_data_file_path(bid_document_file, get_data_path(args.data))
            with open_file(path, mode="rb") as f:
                mime = MimeTypes()
                mime_type = mime.guess_type(path)
                ds_response = ds_client.post_document_upload(
                    {"file": (bid_document_file, f, mime_type[0])}
                )
                bid_documents.append(ds_response.json()["data"])
        with ignore(IOError):
            path = get_data_file_path(bid_file, get_data_path(args.data))
            with open_file_or_exit(path, exit_filename=args.stop) as f:
                bid_create_data = json.loads(f.read())
                bid_create_data["data"]["documents"] = bid_documents
                response = client.post_bid(
                    tender_id,
                    bid_create_data,
                    success_handler=bid_create_success_handler,
                )
                responses.append(response)
    return responses


def create_plans(client, args, filename_prefix=""):
    logging.info("Creating plans...\n")
    plan_files = []
    for data_file in get_data_all_files(get_data_path(args.data)):
        if data_file.startswith("{}plan_create".format(filename_prefix)):
            plan_files.append(data_file)
    responses = []
    for plan_file in plan_files:
        with ignore(IOError):
            path = get_data_file_path(plan_file, get_data_path(args.data))
            with open_file_or_exit(path, exit_filename=args.stop) as f:
                plan_create_data = json.loads(f.read())
                set_mode_data(plan_create_data)
                set_tender_period_data(
                    plan_create_data["data"]["tender"]["tenderPeriod"],
                    acceleration=args.acceleration,
                    client_timedelta=client.client_timedelta,
                )
                response = client.post_plan(
                    plan_create_data, success_handler=plan_create_success_handler
                )
                responses.append(response)
    return responses


def create_plan(client, args, filename_prefix=""):
    logging.info("Creating plan...\n")
    with ignore_silent(IOError):
        path = get_data_file_path(
            "{}plan_create.json".format(filename_prefix), get_data_path(args.data)
        )
        with open_file_or_exit(path, exit_filename=args.stop) as f:
            plan_create_data = json.loads(f.read())
            set_mode_data(plan_create_data)
            set_tender_period_data(
                plan_create_data["data"]["tender"]["tenderPeriod"],
                acceleration=args.acceleration,
                client_timedelta=client.client_timedelta,
            )
            response = client.post_plan(
                plan_create_data, success_handler=plan_create_success_handler
            )
            return response


def patch_plan(client, args, plan_id=None, plan_token=None, filename_prefix=""):
    logging.info("Patching plan...\n")
    with ignore_silent(IOError):
        path = get_data_file_path(
            "{}plan_patch.json".format(filename_prefix), get_data_path(args.data)
        )
        with open_file_or_exit(path, exit_filename=args.stop) as f:
            plan_patch_data = json.loads(f.read())
            response = client.patch_plan(
                plan_id,
                plan_token,
                plan_patch_data,
                success_handler=plan_patch_success_handler,
            )
            return response


def create_tender(client, args, plan_id=None, agreement_id=None, filename_prefix=""):
    logging.info("Creating tender...\n")
    with ignore(IOError):
        path = get_data_file_path(
            "{}tender_create.json".format(filename_prefix), get_data_path(args.data)
        )
        with open_file_or_exit(path, exit_filename=args.stop) as f:
            tender_create_data = json.loads(f.read())
            set_mode_data(tender_create_data["data"])
            set_acceleration_data(
                tender_create_data["data"],
                acceleration=args.acceleration,
                submission=args.submission,
            )
            if agreement_id:
                tender_create_data["data"]["agreements"] = [{"id": agreement_id}]
            if plan_id:
                response = client.post_tender(
                    plan_id,
                    tender_create_data,
                    success_handler=tender_create_success_handler,
                )
            else:
                response = client.post_tender(
                    tender_create_data, success_handler=tender_create_success_handler
                )
            return response


def extend_tender_period(
    tender_period, client, args, tender_id, tender_token, period_timedelta
):
    data = {"data": {"tenderPeriod": {"endDate": DATETIME_MASK}}}
    set_tender_period_data(
        data["data"]["tenderPeriod"],
        acceleration=args.acceleration,
        min_period_timedelta=period_timedelta,
        client_timedelta=client.client_timedelta,
    )
    if (
        tender_period
        and tender_period["endDate"] < data["data"]["tenderPeriod"]["endDate"]
    ):
        response = client.patch_tender(
            tender_id,
            tender_token,
            data,
            success_handler=tender_patch_period_success_handler,
        )
        return response


def extend_tender_period_min(tender_period, client, args, tender_id, tender_token):
    return extend_tender_period(
        tender_period=tender_period,
        client=client,
        args=args,
        tender_id=tender_id,
        tender_token=tender_token,
        period_timedelta=TENDER_PERIOD_MIN_TIMEDELTA,
    )


def wait(date_str, client_timedelta=timedelta(), date_info_str=None):
    now = fix_datetime(
        get_utcnow(),
        client_timedelta,
    )
    date_timedelta = parse_date(date_str) - now
    delta_seconds = date_timedelta.total_seconds()
    date_seconds = math.ceil(delta_seconds) if delta_seconds > 0 else 0
    info_str = " for {}".format(date_info_str) if date_info_str else ""
    logging.info(
        "Waiting {} seconds{} - {}...\n".format(date_seconds, info_str, date_str)
    )
    sleep(date_seconds)


def wait_status(client, args, tender_id, status, fallback=None):
    logging.info("Waiting for {}...\n".format(status))
    if not isinstance(status, list):
        status = [status]
    while True:
        response = client.get_tender(tender_id)
        if response.json()["data"]["status"] not in status:
            sleep(TENDER_SECONDS_BUFFER)
            if fallback:
                fallback()
        else:
            response_handler(response, tender_check_status_success_handler)
            break
    return response


def patch_stage2_credentials(client, args, stage2_tender_id, tender_token):
    logging.info("Getting credentials for second stage...\n")
    with ignore(IOError):
        path = get_data_file_path(
            "stage2_tender_credentials.json", get_data_path(args.data)
        )
        with open_file_or_exit(path, exit_filename=args.stop) as f:
            tender_patch_data = json.loads(f.read())
            return client.patch_credentials(
                stage2_tender_id,
                tender_token,
                tender_patch_data,
                success_handler=tender_create_success_handler,
            )


def patch_contract_credentials(client, args, contract_id, tender_token):
    logging.info("Getting credentials for contract...\n")
    return client.patch_credentials(
        contract_id,
        tender_token,
        {},
        success_handler=contract_credentials_success_handler,
    )


def patch_tender_tendering(client, args, tender_id, tender_token, filename_prefix=""):
    logging.info("Activating tender by switching to next status...\n")
    with ignore(IOError):
        path = get_data_file_path(
            "{}tender_patch_tendering.json".format(filename_prefix),
            get_data_path(args.data),
        )
        with open_file_or_exit(path, exit_filename=args.stop) as f:
            tender_patch_data = json.loads(f.read())
            return client.patch_tender(
                tender_id,
                tender_token,
                tender_patch_data,
                success_handler=tender_patch_success_handler,
            )


def patch_tender_pending(client, args, tender_id, tender_token, filename_prefix=""):
    logging.info("Activating tender by switching to next status...\n")
    with ignore(IOError):
        path = get_data_file_path(
            "{}tender_patch_pending.json".format(filename_prefix),
            get_data_path(args.data),
        )
        with open_file_or_exit(path, exit_filename=args.stop) as f:
            tender_patch_data = json.loads(f.read())
            return client.patch_tender(
                tender_id,
                tender_token,
                tender_patch_data,
                success_handler=tender_patch_success_handler,
            )


def post_criteria(client, args, tender_id, tender_token, filename_prefix=""):
    logging.info("Create tender criteria...\n")
    with ignore(IOError):
        path = get_data_file_path(
            "{}criteria_create.json".format(filename_prefix), get_data_path(args.data)
        )
        with open_file_or_exit(path, exit_filename=args.stop) as f:
            criteria_data = json.loads(f.read())
            return client.post_criteria(
                tender_id,
                tender_token,
                criteria_data,
                success_handler=tender_post_criteria_success_handler,
            )


def patch_tender(client, args, tender_id, tender_token, filename_prefix=""):
    logging.info("Patching tender...\n")
    with ignore(IOError):
        path = get_data_file_path(
            "{}tender_patch.json".format(filename_prefix), get_data_path(args.data)
        )
        with open_file_or_exit(path, exit_filename=args.stop) as f:
            tender_patch_data = json.loads(f.read())
            return client.patch_tender(
                tender_id,
                tender_token,
                tender_patch_data,
                success_handler=tender_patch_success_handler,
            )


def wait_edr_pre_qual(client, args, tender_id):
    logging.info("Waiting for {} in qualifications documents...\n".format(EDR_FILENAME))
    response = get_qualifications(client, args, tender_id)
    for qualification in response.json()["data"]:
        while EDR_FILENAME not in [
            doc["title"] for doc in qualification.get("documents", [])
        ]:
            sleep(TENDER_SECONDS_BUFFER)
            qualification = client.get_qualification(
                tender_id, qualification["id"]
            ).json()["data"]


def wait_edr_qual(client, args, tender_id):
    logging.info("Waiting for {} in awards documents...\n".format(EDR_FILENAME))
    response = get_awards(client, args, tender_id)
    for award in response.json()["data"]:
        while EDR_FILENAME not in [doc["title"] for doc in award.get("documents", [])]:
            sleep(TENDER_SECONDS_BUFFER)
            award = client.get_award(tender_id, award["id"]).json()["data"]


def wait_auction_participation_urls(client, tender_id, bids):
    logging.info("Waiting for the auction participation urls...\n")
    for bid in bids:
        while True:
            response = client.get_bid(
                tender_id, bid["data"]["id"], bid["access"]["token"]
            )
            if bid.get("status") == "unsuccessful":
                break
            if "lotValues" in response.json()["data"]:
                if all(
                    [
                        "participationUrl" in lot_value
                        for lot_value in response.json()["data"]["lotValues"]
                        if lot_value["status"] == "active"
                    ]
                ):
                    response_handler(
                        response, auction_multilot_participation_url_success_handler
                    )
                    break
                else:
                    sleep(TENDER_SECONDS_BUFFER)
            else:
                if "participationUrl" in response.json()["data"]:
                    response_handler(
                        response, auction_participation_url_success_handler
                    )
                    break
                else:
                    sleep(TENDER_SECONDS_BUFFER)


def post_tender_plan(
    client, args, tender_id, tender_token, plan_id, filename_prefix=""
):
    logging.info("Connecting plan to tender...\n")
    tender_patch_data = {"data": {"id": plan_id}}
    return client.post_plan(
        tender_id,
        tender_token,
        tender_patch_data,
        success_handler=tender_post_plan_success_handler,
    )
