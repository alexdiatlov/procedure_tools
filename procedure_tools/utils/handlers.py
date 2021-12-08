import logging

from procedure_tools.utils.style import (
    fore,
    fore_success,
    fore_warning,
    fore_error,
    fore_status_code,
)

EX_OK = 0
EX_DATAERR = 65


def default_error_handler(response):
    msg = "Response text:\n"
    msg += fore_error(response.text)
    logging.info(msg)
    raise SystemExit(EX_DATAERR)


def default_success_handler(response):
    pass


def response_handler(
    response,
    success_handler=default_success_handler,
    error_handler=default_error_handler,
):
    msg = "Response status code: "
    msg += fore_status_code(response.status_code)
    msg += "\n"
    logging.info(msg)
    if 200 <= response.status_code < 300:
        success_handler(response)
    else:
        error_handler(response)


def client_init_response_handler(
    response,
    client_timedelta,
):
    response_handler(response)
    logging.info(
        "Client time delta with server: {} seconds\n".format(
            int(client_timedelta.total_seconds())
        ),
    )


def tender_create_success_handler(response):
    data = response.json()["data"]
    access = response.json()["access"]

    msg = "Tender created:\n"
    msg += " - id \t\t\t\t{}\n".format(fore_success(data["id"]))
    msg += " - token \t\t\t{}\n".format(fore_success(access["token"]))
    if "transfer" in access:
        msg += " - transfer \t\t\t{}\n".format(fore_success(access["transfer"]))
    msg += " - status \t\t\t{}\n".format(fore_success(data["status"]))
    msg += " - tenderID \t\t\t{}\n".format(fore_success(data["tenderID"]))
    msg += " - procurementMethodType \t{}\n".format(
        fore_success(data["procurementMethodType"])
    )

    logging.info(msg)


def plan_create_success_handler(response):
    data = response.json()["data"]
    access = response.json()["access"]

    msg = "Plan created:\n"
    msg += " - id \t\t\t\t{}\n".format(fore_success(data["id"]))
    msg += " - token \t\t\t{}\n".format(fore_success(access["token"]))
    if "transfer" in access:
        msg += " - transfer \t\t\t{}\n".format(fore_success(access["transfer"]))

    logging.info(msg)


def contract_credentials_success_handler(response):
    data = response.json()["data"]
    access = response.json()["access"]

    msg = "Contract patched:\n"
    msg += " - id \t\t\t\t{}\n".format(fore_success(data["id"]))
    msg += " - token \t\t\t{}\n".format(fore_success(access["token"]))

    logging.info(msg)


def bid_create_success_handler(response):
    data = response.json()["data"]
    access = response.json()["access"]

    msg = "Bid created:\n"
    msg += " - id \t\t\t\t{}\n".format(fore_success(data["id"]))
    msg += " - token \t\t\t{}\n".format(fore_success(access["token"]))
    msg += " - status \t\t\t{}\n".format(fore_success(data["status"]))

    logging.info(msg)


def item_create_success_handler(response):
    data = response.json()["data"]

    msg = "Item created:\n"
    msg += " - id \t\t\t\t{}\n".format(fore_success(data["id"]))
    msg += " - status \t\t\t{}\n".format(fore_success(data["status"]))

    logging.info(msg)


def item_get_success_handler(response):
    data = response.json()["data"]
    for item in data:
        msg = "Item found:\n"
        msg += " - id \t\t\t\t{}\n".format(fore_success(data["id"]))
        msg += " - status \t\t\t{}\n".format(fore_success(item["status"]))

        logging.info(msg)


def item_patch_success_handler(response):
    data = response.json()["data"]

    msg = "Item patched:\n"
    msg += " - id \t\t\t\t{}\n".format(fore_success(data["id"]))
    msg += " - status \t\t\t{}\n".format(fore_success(data["status"]))

    logging.info(msg)


def tender_patch_success_handler(response):
    data = response.json()["data"]

    msg = "Tender patched:\n"
    msg += " - id \t\t\t\t{}\n".format(fore_success(data["id"]))
    msg += " - status \t\t\t{}\n".format(fore_success(data["status"]))

    logging.info(msg)


def tender_post_criteria_success_handler(response):
    data = response.json()["data"]

    msg = "Tender criteria created:\n"
    for item in data:
        msg += " - classification.id \t\t\t\t{}\n".format(
            fore_success(item["classification"]["id"])
        )

    logging.info(msg)


def tender_check_status_success_handler(response):
    data = response.json()["data"]

    msg = "Tender info:\n"
    msg += " - id \t\t\t\t{}\n".format(fore_success(data["id"]))
    msg += " - status \t\t\t{}\n".format(fore_success(data["status"]))

    logging.info(msg)


def auction_participation_url_success_handler(response):
    data = response.json()["data"]

    msg = "Auction participation url for bid:\n"
    msg += " - id \t\t\t\t{}\n".format(fore_success(data["id"]))
    msg += " - url \t\t\t{}\n".format(fore_success(data["participationUrl"]))

    logging.info(msg)


def auction_multilot_participation_url_success_handler(response):
    data = response.json()["data"]

    msg = "Auction participation url for bid:\n"
    msg += " - id \t\t\t\t{}\n".format(fore_success(data["id"]))
    for lot_value in response.json()["data"]["lotValues"]:
        msg += "Lot:\n"
        msg += " - relatedLot\t\t\t{}\n".format(fore_success(lot_value["relatedLot"]))
        msg += " - url \t\t\t\t{}\n".format(fore_success(lot_value["participationUrl"]))

    logging.info(msg)


def tender_patch_period_success_handler(response):
    data = response.json()["data"]

    msg = "Tender patched:\n"
    msg += " - tenderPeriod.startDate \t{}\n".format(
        fore_success(data["tenderPeriod"]["startDate"])
    )
    msg += " - tenderPeriod.endDate \t{}\n".format(
        fore_success(data["tenderPeriod"]["endDate"])
    )

    logging.info(msg)


def tender_post_plan_success_handler(response):
    data = response.json()["data"]

    msg = "Tender plans:\n"
    for plan in response.json()["data"]:
        msg += " - id \t\t\t\t{}\n".format(fore_success(plan["id"]))

    logging.info(msg)