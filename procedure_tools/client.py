from __future__ import absolute_import

import json
import logging
from copy import deepcopy, copy
from base64 import b64encode
from datetime import timedelta

from procedure_tools.utils.date import get_utcnow, parse_date_header

try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

import requests

from procedure_tools.utils import adapters
from procedure_tools.utils.handlers import (
    response_handler,
    client_init_response_handler,
)
from procedure_tools.version import __version__

API_PATH_PREFIX_DEFAULT = "/api/0/"


class BaseApiClient(object):
    SPORE_PATH = "spore"

    HEADERS_DEFAULT = {
        "User-Agent": "procedure_tools/{}".format(__version__),
    }

    def __init__(self, host, session=None, debug=False, **kwargs):
        self.host = host
        self.kwargs = kwargs
        self.debug = debug
        if session:
            self.session = session
        else:
            self.session = requests.Session()
            adapters.mount(session)
        self.set_default_kwargs()

    def set_default_kwargs(self):
        headers = copy(self.HEADERS_DEFAULT)
        headers.update(self.kwargs.pop("headers", {}))
        self.kwargs.update(dict(headers=headers))

    @staticmethod
    def pop_handlers(kwargs, success_handler=None, error_handler=None):
        return dict(
            (k, v)
            for k, v in dict(
                success_handler=kwargs.pop("success_handler", success_handler),
                error_handler=kwargs.pop("error_handler", error_handler),
            ).items()
            if v is not None
        )

    def get_url(self, api_path):
        return urljoin(self.host, api_path)

    def format_data(self, data):
        try:
            text = json.dumps(data, ensure_ascii=False, indent=4)
        except TypeError:
            text = str(data)
        return text

    def log_request(self, data):
        if data is not None:
            request_text = self.format_data(data)
            logging.debug(f"Request:\n {request_text}")

    def log_response(self, text):
        if text is not None:
            try:
                data = json.loads(text)
            except json.JSONDecodeError:
                response_text = text
            else:
                response_text = self.format_data(data)
            logging.debug(f"Response:\n {response_text}")

    def request(self, method, path, **kwargs):
        request_kwargs = deepcopy(self.kwargs)
        handlers = self.pop_handlers(kwargs)
        request_kwargs.update(kwargs)
        url = self.get_url(path)
        response = self.session.request(method=method, url=url, **request_kwargs)
        if self.debug:
            self.log_request(request_kwargs.get("json", None))
            self.log_response(response.text)
        response_handler(response, **handlers)
        return response

    def get(self, path, **kwargs):
        return self.request("GET", path, **kwargs)

    def post(self, path, json=None, **kwargs):
        return self.request("POST", path, json=json, **kwargs)

    def patch(self, path, json=None, **kwargs):
        return self.request("PATCH", path, json=json, **kwargs)


class BaseCDBClient(BaseApiClient):
    SPORE_PATH = "spore"

    def __init__(
        self,
        host,
        auth_token=None,
        path_prefix=API_PATH_PREFIX_DEFAULT,
        session=None,
        **request_kwargs,
    ):
        super(BaseCDBClient, self).__init__(host, session=session, **request_kwargs)
        self.path_prefix = path_prefix
        self.set_kwargs(auth_token)
        spore_url = self.get_url(self.get_api_path(self.SPORE_PATH))
        # GET request to retrieve SERVER_ID cookie and server time
        response = self.session.get(spore_url)
        client_datetime = get_utcnow()
        try:
            server_datetime = parse_date_header(response.headers.get("date"))
            self.client_timedelta = server_datetime - client_datetime
        except:
            self.client_timedelta = timedelta()
        client_init_response_handler(response, self.client_timedelta)

    def set_kwargs(self, auth_token):
        self.kwargs["headers"].update({"Content-Type": "application/json"})
        if auth_token:
            self.kwargs["headers"].update({"Authorization": "Bearer " + auth_token})

    def get_api_path(self, path, acc_token=None):
        return urljoin(
            self.path_prefix,
            urljoin(path, "?acc_token={}".format(acc_token) if acc_token else None),
        )


class TendersApiClient(BaseCDBClient):
    TENDERS_COLLECTION_PATH = "tenders"
    TENDERS_PATH = "tenders/{}"
    TENDERS_DOCUMENTS_COLLECTION_PATH = "tenders/{}/documents"
    PLANS_PATH = "tenders/{}/plans"
    CRITERIA_COLLECTION_PATH = "tenders/{}/criteria"
    BIDS_COLLECTION_PATH = "tenders/{}/bids"
    BIDS_PATH = "tenders/{}/bids/{}"
    BIDS_RES_COLLECTION_PATH = "tenders/{}/bids/{}/requirement_responses"
    AWARDS_COLLECTION_PATH = "tenders/{}/awards"
    AWARDS_PATH = "tenders/{}/awards/{}"
    CONTRACTS_COLLECTION_PATH = "tenders/{}/contracts"
    CONTRACTS_PATH = "tenders/{}/contracts/{}"
    CONTRACT_UNIT_VALUE_PATH = "tenders/{}/contracts/{}/items/{}/unit/value"
    QUALIFICATIONS_COLLECTION_PATH = "tenders/{}/qualifications"
    QUALIFICATIONS_PATH = "tenders/{}/qualifications/{}"
    AGREEMENTS_COLLECTION_PATH = "tenders/{}/agreements"
    AGREEMENTS_PATH = "tenders/{}/agreements/{}"
    AGREEMENTS_DOCUMENTS_COLLECTION_PATH = "tenders/{}/agreements/{}/documents"
    AGREEMENTS_CONTRACTS_COLLECTION_PATH = "tenders/{}/agreements/{}/contracts"
    AGREEMENTS_CONTRACTS_PATH = "tenders/{}/agreements/{}/contracts/{}"
    CREDENTIALS_PATH = "tenders/{}/credentials"
    COMPLAINTS_COLLECTION_PATH = "tenders/{}/complaints"
    COMPLAINTS_PATH = "tenders/{}/complaints/{}"

    def get_tender(self, tender_id, **kwargs):
        tenders_path = self.TENDERS_PATH.format(tender_id)
        path = self.get_api_path(tenders_path)
        return self.get(path, **kwargs)

    def post_tender(self, json, **kwargs):
        tenders_path = self.TENDERS_COLLECTION_PATH
        path = self.get_api_path(tenders_path)
        return self.post(path, json, **kwargs)

    def patch_tender(self, tender_id, acc_token, json, **kwargs):
        tenders_path = self.TENDERS_PATH.format(tender_id)
        path = self.get_api_path(tenders_path, acc_token=acc_token)
        return self.patch(path, json, **kwargs)

    def post_tender_document(self, tender_id, acc_token, json, **kwargs):
        documents_path = self.TENDERS_DOCUMENTS_COLLECTION_PATH.format(tender_id)
        path = self.get_api_path(documents_path, acc_token=acc_token)
        return self.post(path, json, **kwargs)

    def post_plan(self, tender_id, acc_token, json, **kwargs):
        tenders_path = self.PLANS_PATH.format(tender_id)
        path = self.get_api_path(tenders_path, acc_token=acc_token)
        return self.post(path, json, **kwargs)

    def post_criteria(self, tender_id, acc_token, json, **kwargs):
        criteria_path = self.CRITERIA_COLLECTION_PATH.format(tender_id)
        path = self.get_api_path(criteria_path, acc_token=acc_token)
        return self.post(path, json, **kwargs)

    def get_bids(self, tender_id, **kwargs):
        bid_path = self.BIDS_COLLECTION_PATH.format(tender_id)
        path = self.get_api_path(bid_path)
        return self.get(path, **kwargs)

    def get_bid(self, tender_id, bid_id, acc_token, **kwargs):
        bid_path = self.BIDS_PATH.format(tender_id, bid_id)
        path = self.get_api_path(bid_path, acc_token=acc_token)
        return self.get(path, **kwargs)

    def post_bid(self, tender_id, json, **kwargs):
        bids_path = self.BIDS_COLLECTION_PATH.format(tender_id)
        path = self.get_api_path(bids_path)
        return self.post(path, json, **kwargs)

    def patch_bid(self, tender_id, bid_id, acc_token, json, **kwargs):
        bid_path = self.BIDS_PATH.format(tender_id, bid_id)
        path = self.get_api_path(bid_path, acc_token=acc_token)
        return self.patch(path, json, **kwargs)

    def post_bid_res(self, tender_id, bid_id, acc_token, json, **kwargs):
        bid_res_path = self.BIDS_RES_COLLECTION_PATH.format(tender_id, bid_id)
        path = self.get_api_path(bid_res_path, acc_token=acc_token)
        return self.post(path, json, **kwargs)

    def get_complaints(self, tender_id, **kwargs):
        complaints_path = self.COMPLAINTS_COLLECTION_PATH.format(tender_id)
        path = self.get_api_path(complaints_path)
        return self.get(path, **kwargs)

    def get_complaint(self, tender_id, complaint_id, **kwargs):
        complaints_path = self.COMPLAINTS_PATH.format(tender_id, complaint_id)
        path = self.get_api_path(complaints_path)
        return self.get(path, **kwargs)

    def post_complaint(self, tender_id, acc_token, json, **kwargs):
        complaints_path = self.COMPLAINTS_COLLECTION_PATH.format(tender_id)
        path = self.get_api_path(complaints_path, acc_token=acc_token)
        return self.post(path, json, **kwargs)

    def patch_complaint(self, tender_id, complaint_id, acc_token, json, **kwargs):
        complaints_path = self.COMPLAINTS_PATH.format(
            tender_id, complaint_id, acc_token
        )
        path = self.get_api_path(complaints_path, acc_token=acc_token)
        return self.patch(path, json, **kwargs)

    def get_qualifications(self, tender_id, **kwargs):
        qualifications_path = self.QUALIFICATIONS_COLLECTION_PATH.format(tender_id)
        path = self.get_api_path(qualifications_path)
        return self.get(path, **kwargs)

    def get_qualification(self, tender_id, qualification_id, **kwargs):
        qualifications_path = self.QUALIFICATIONS_PATH.format(
            tender_id, qualification_id
        )
        path = self.get_api_path(qualifications_path)
        return self.get(path, **kwargs)

    def patch_qualification(
        self, tender_id, qualification_id, acc_token, json, **kwargs
    ):
        qualifications_path = self.QUALIFICATIONS_PATH.format(
            tender_id, qualification_id, acc_token
        )
        path = self.get_api_path(qualifications_path, acc_token=acc_token)
        return self.patch(path, json, **kwargs)

    def get_awards(self, tender_id, **kwargs):
        awards_path = self.AWARDS_COLLECTION_PATH.format(tender_id)
        path = self.get_api_path(awards_path)
        return self.get(path, **kwargs)

    def get_award(self, tender_id, award_id, **kwargs):
        awards_path = self.AWARDS_PATH.format(tender_id, award_id)
        path = self.get_api_path(awards_path)
        return self.get(path, **kwargs)

    def post_award(self, tender_id, acc_token, json, **kwargs):
        awards_path = self.AWARDS_COLLECTION_PATH.format(tender_id)
        path = self.get_api_path(awards_path, acc_token=acc_token)
        return self.post(path, json, **kwargs)

    def patch_award(self, tender_id, award_id, acc_token, json, **kwargs):
        awards_path = self.AWARDS_PATH.format(tender_id, award_id, acc_token)
        path = self.get_api_path(awards_path, acc_token=acc_token)
        return self.patch(path, json, **kwargs)

    def get_contracts(self, tender_id, **kwargs):
        awards_path = self.CONTRACTS_COLLECTION_PATH.format(tender_id)
        path = self.get_api_path(awards_path)
        return self.get(path, **kwargs)

    def patch_contract(self, tender_id, contract_id, acc_token, json, **kwargs):
        awards_path = self.CONTRACTS_PATH.format(tender_id, contract_id, acc_token)
        path = self.get_api_path(awards_path, acc_token=acc_token)
        return self.patch(path, json, **kwargs)

    def patch_contract_unit_value(
        self, tender_id, contract_id, item_id, acc_token, json, **kwargs
    ):
        awards_path = self.CONTRACT_UNIT_VALUE_PATH.format(
            tender_id, contract_id, item_id, acc_token
        )
        path = self.get_api_path(awards_path, acc_token=acc_token)
        return self.patch(path, json, **kwargs)

    def get_agreements(self, tender_id, **kwargs):
        agreements_path = self.AGREEMENTS_COLLECTION_PATH.format(tender_id)
        path = self.get_api_path(agreements_path)
        return self.get(path, **kwargs)

    def patch_agreement(self, tender_id, agreement_id, acc_token, json, **kwargs):
        agreements_path = self.AGREEMENTS_PATH.format(
            tender_id, agreement_id, acc_token
        )
        path = self.get_api_path(agreements_path, acc_token=acc_token)
        return self.patch(path, json, **kwargs)

    def post_agreement_document(
        self, tender_id, agreement_id, acc_token, json, **kwargs
    ):
        agreements_path = self.AGREEMENTS_DOCUMENTS_COLLECTION_PATH.format(
            tender_id, agreement_id
        )
        path = self.get_api_path(agreements_path, acc_token=acc_token)
        return self.post(path, json, **kwargs)

    def get_agreement_contracts(self, tender_id, agreement_id, **kwargs):
        agreement_contracts_path = self.AGREEMENTS_CONTRACTS_COLLECTION_PATH.format(
            tender_id, agreement_id
        )
        path = self.get_api_path(agreement_contracts_path)
        return self.get(path, **kwargs)

    def patch_agreement_contract(
        self, tender_id, agreement_id, contract_id, acc_token, json, **kwargs
    ):
        agreement_contracts_path = self.AGREEMENTS_CONTRACTS_PATH.format(
            tender_id, agreement_id, contract_id, acc_token
        )
        path = self.get_api_path(agreement_contracts_path, acc_token=acc_token)
        return self.patch(path, json, **kwargs)

    def patch_credentials(self, tender_id, acc_token, json, **kwargs):
        credentials_path = self.CREDENTIALS_PATH.format(tender_id)
        path = self.get_api_path(credentials_path, acc_token=acc_token)
        return self.patch(path, json, **kwargs)


class AgreementsApiClient(BaseCDBClient):
    AGREEMENTS_PATH = "agreements/{}"

    def get_agreement(self, agreement_id, **kwargs):
        agreements_path = self.AGREEMENTS_PATH.format(agreement_id)
        path = self.get_api_path(agreements_path)
        return self.get(path, **kwargs)


class ContractsApiClient(BaseCDBClient):
    CONTRACTS_PATH = "contracts/{}"
    CREDENTIALS_PATH = "contracts/{}/credentials"

    def get_contract(self, contract_id, **kwargs):
        contracts_path = self.CONTRACTS_PATH.format(contract_id)
        path = self.get_api_path(contracts_path)
        return self.get(path, **kwargs)

    def patch_credentials(self, contract_id, acc_token, json, **kwargs):
        credentials_path = self.CREDENTIALS_PATH.format(contract_id)
        path = self.get_api_path(credentials_path, acc_token=acc_token)
        return self.patch(path, json, **kwargs)


class PlansApiClient(BaseCDBClient):
    PLANS_COLLECTION_PATH = "plans"
    PLANS_PATH = "plans/{}"
    TENDERS_COLLECTION_PATH = "plans/{}/tenders"

    def get_plan(self, plan_id, **kwargs):
        contracts_path = self.PLANS_PATH.format(plan_id)
        path = self.get_api_path(contracts_path)
        return self.get(path, **kwargs)

    def post_plan(self, json, **kwargs):
        tenders_path = self.PLANS_COLLECTION_PATH
        path = self.get_api_path(tenders_path)
        return self.post(path, json, **kwargs)

    def patch_plan(self, plan_id, acc_token, json, **kwargs):
        tenders_path = self.PLANS_PATH.format(plan_id)
        path = self.get_api_path(tenders_path, acc_token=acc_token)
        return self.patch(path, json, **kwargs)

    def post_tender(self, plan_id, json, **kwargs):
        tenders_path = self.TENDERS_COLLECTION_PATH.format(plan_id)
        path = self.get_api_path(tenders_path)
        return self.post(path, json, **kwargs)


class DsApiClient(BaseApiClient):
    UPLOAD_PATH = "upload"

    def __init__(
        self, host, username=None, password=None, session=None, **request_kwargs
    ):
        super(DsApiClient, self).__init__(host, session=session, **request_kwargs)
        self.set_kwargs(username, password)

    def set_kwargs(self, username, password):
        if username and password:
            self.kwargs["headers"].update(
                {
                    "Authorization": "Basic "
                    + b64encode("{}:{}".format(username, password).encode()).decode()
                }
            )

    def post_document_upload(self, files, **kwargs):
        path = self.UPLOAD_PATH
        return self.post(path, files=files, **kwargs)
