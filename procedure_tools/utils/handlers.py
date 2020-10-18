import json
import logging

EX_OK = 0
EX_DATAERR = 65


def default_error_handler(response):
    try:
        logging.info(json.loads(response.text))
    except ValueError:
        logging.info(response.text)
    raise SystemExit(EX_DATAERR)


def default_success_handler(response):
    pass


def response_handler(
    response,
    success_handler=default_success_handler,
    error_handler=default_error_handler
):
    logging.info("[{}] {}\n".format(
        response.request.method,
        response.request.url
    ))
    if response.status_code in [200, 201]:
        success_handler(response)
    else:
        error_handler(response)


def tender_create_success_handler(response):
    data = response.json()["data"]
    access = response.json()["access"]

    msg = "Tender created:\n"
    msg += " - id \t\t\t\t{}\n".format(data["id"])
    msg += " - token \t\t\t{}\n".format(access["token"])
    if "transfer" in access:
        msg += " - transfer \t\t\t{}\n".format(access["transfer"])
    msg += " - status \t\t\t{}\n".format(data["status"])
    msg += " - tenderID \t\t\t{}\n".format(data["tenderID"])
    msg += " - tenderID \t\t\t{}\n".format(data["tenderID"])
    msg += " - procurementMethodType \t{}\n".format(data["procurementMethodType"])

    logging.info(msg)


def plan_create_success_handler(response):
    data = response.json()["data"]
    access = response.json()["access"]

    msg = "Plan created:\n"
    msg += " - id \t\t\t\t{}\n".format(data["id"])
    msg += " - token \t\t\t{}\n".format(access["token"])
    if "transfer" in access:
        msg += " - transfer \t\t\t{}\n".format(access["transfer"])

    logging.info(msg)


def contract_credentials_success_handler(response):
    data = response.json()["data"]
    access = response.json()["access"]

    msg = "Contract patched:\n"
    msg += " - id \t\t\t\t{}\n".format(data["id"])
    msg += " - token \t\t\t{}\n".format(access["token"])

    logging.info(msg)


def bid_create_success_handler(response):
    data = response.json()["data"]
    access = response.json()["access"]

    msg = "Bid created:\n"
    msg += " - id \t\t\t\t{}\n".format(data["id"])
    msg += " - token \t\t\t{}\n".format(access["token"])
    msg += " - status \t\t\t{}\n".format(data["status"])

    logging.info(msg)


def item_create_success_handler(response):
    data = response.json()["data"]

    msg = "Item created:\n"
    msg += " - id \t\t\t\t{}\n".format(data["id"])
    msg += " - status \t\t\t{}\n".format(data["status"])

    logging.info(msg)


def item_get_success_handler(response):
    data = response.json()["data"]
    for item in data:
        msg = "Item found:\n"
        msg += " - id \t\t\t\t{}\n".format(data["id"])
        msg += " - status \t\t\t{}\n".format(item["status"])

        logging.info(msg)


def item_patch_success_handler(response):
    data = response.json()["data"]

    msg = "Item patched:\n"
    msg += " - id \t\t\t\t{}\n".format(data["id"])
    msg += " - status \t\t\t{}\n".format(data["status"])

    logging.info(msg)


def tender_patch_status_success_handler(response):
    data = response.json()["data"]

    msg = "Tender status patched:\n"
    msg += " - id \t\t\t\t{}\n".format(data["id"])
    msg += " - status \t\t\t{}\n".format(data["status"])

    logging.info(msg)


def tender_post_criteria_success_handler(response):
    data = response.json()["data"]

    msg = "Tender criteria created:\n"
    for item in data:
        msg += " - classification.id \t\t\t\t{}\n".format(item["classification"]["id"])

    logging.info(msg)


def tender_check_status_success_handler(response):
    data = response.json()["data"]

    msg = "Tender info:\n"
    msg += " - id \t\t\t\t{}\n".format(data["id"])
    msg += " - status \t\t\t{}\n".format(data["status"])

    logging.info(msg)


def auction_participation_url_success_handler(response):
    data = response.json()["data"]

    msg = "Auction participation url for bid:\n"
    msg += " - id \t\t\t\t{}\n".format(data["id"])
    msg += " - url \t\t\t{}\n".format(data["participationUrl"])

    logging.info(msg)
