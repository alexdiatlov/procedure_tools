from __future__ import absolute_import

from copy import deepcopy
from base64 import b64encode

from requests.adapters import HTTPAdapter

try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

import requests

from procedure_tools.utils.handlers import response_handler

API_PATH_PREFIX_DEFAULT = "/api/0/"


class BaseApiClient(object):
    SPORE_PATH = "spore"

    def __init__(self, host, session=None, **request_kwargs):
        self.host = host
        self.kwargs = request_kwargs
        if session:
            self.session = session
        else:
            self.session = requests.Session()

    @staticmethod
    def _pop_handlers(kwargs, success_handler=None, error_handler=None):
        return dict(
            (k, v)
            for k, v in dict(
                success_handler=kwargs.pop("success_handler", success_handler),
                error_handler=kwargs.pop("error_handler", error_handler),
            ).items()
            if v is not None
        )

    def _get_url(self, api_path):
        return urljoin(self.host, api_path)

    def get(self, path, **kwargs):
        request_kwargs = deepcopy(self.kwargs)
        handlers = self._pop_handlers(kwargs)
        request_kwargs.update(kwargs)
        url = self._get_url(path)
        response = self.session.get(url=url, **request_kwargs)
        response_handler(response, **handlers)
        return response

    def post(self, path, json=None, **kwargs):
        request_kwargs = deepcopy(self.kwargs)
        handlers = self._pop_handlers(kwargs)
        request_kwargs.update(kwargs)
        url = self._get_url(path)
        response = self.session.post(url=url, json=json, **request_kwargs)
        response_handler(response, **handlers)
        return response

    def patch(self, path, json=None, **kwargs):
        request_kwargs = deepcopy(self.kwargs)
        handlers = self._pop_handlers(kwargs)
        request_kwargs.update(kwargs)
        url = self._get_url(path)
        response = self.session.patch(url=url, json=json, **request_kwargs)
        response_handler(response, **handlers)
        return response


class BaseCDBClient(BaseApiClient):
    SPORE_PATH = "spore"
    HEADERS_DEFAULT = {"Content-Type": "application/json"}

    def __init__(self, host, auth_token=None, path_prefix=API_PATH_PREFIX_DEFAULT, session=None, **request_kwargs):
        super(BaseCDBClient, self).__init__(host, session=session, **request_kwargs)
        self.path_prefix = path_prefix
        self._set_headers(request_kwargs, auth_token)
        self._init_session(request_kwargs)

    def _set_headers(self, request_kwargs, auth_token):
        headers = self.HEADERS_DEFAULT
        headers.update(request_kwargs.pop("headers", {}))
        if auth_token:
            headers.update({"Authorization": "Bearer " + auth_token})
        request_kwargs.update(dict(headers=headers))
        self.kwargs.update(request_kwargs)

    def _init_session(self, request_kwargs):
        spore_url = self._get_url(self._get_api_path(self.SPORE_PATH))
        self.session.get(spore_url)  # GET request to retrieve SERVER_ID cookie

    def _get_api_path(self, path, acc_token=None):
        return urljoin(self.path_prefix, urljoin(path, "?acc_token={}".format(acc_token) if acc_token else None))


class TendersApiClient(BaseCDBClient):
    TENDERS_COLLECTION_PATH = "tenders"
    TENDERS_PATH = "tenders/{}"
    CRITERIA_COLLECTION_PATH = "tenders/{}/criteria"
    BIDS_COLLECTION_PATH = "tenders/{}/bids"
    BIDS_PATH = "tenders/{}/bids/{}"
    BIDS_RES_COLLECTION_PATH = "tenders/{}/bids/{}/requirement_responses"
    AWARDS_COLLECTION_PATH = "tenders/{}/awards"
    AWARDS_PATH = "tenders/{}/awards/{}"
    CONTRACTS_COLLECTION_PATH = "tenders/{}/contracts"
    CONTRACTS_PATH = "tenders/{}/contracts/{}"
    QUALIFICATIONS_COLLECTION_PATH = "tenders/{}/qualifications"
    QUALIFICATIONS_PATH = "tenders/{}/qualifications/{}"
    AGREEMENTS_COLLECTION_PATH = "tenders/{}/agreements"
    AGREEMENTS_PATH = "tenders/{}/agreements/{}"
    AGREEMENT_CONTRACT_COLLECTION_PATH = "tenders/{}/agreements/{}/contracts"
    AGREEMENT_CONTRACT_PATH = "tenders/{}/agreements/{}/contracts/{}"
    CREDENTIALS_PATH = "tenders/{}/credentials"

    def get_tender(self, tender_id, **kwargs):
        tenders_path = self.TENDERS_PATH.format(tender_id)
        path = self._get_api_path(tenders_path)
        return self.get(path, **kwargs)

    def post_tender(self, json, **kwargs):
        tenders_path = self.TENDERS_COLLECTION_PATH
        path = self._get_api_path(tenders_path)
        return self.post(path, json, **kwargs)

    def patch_tender(self, tender_id, acc_token, json, **kwargs):
        tenders_path = self.TENDERS_PATH.format(tender_id)
        path = self._get_api_path(tenders_path, acc_token=acc_token)
        return self.patch(path, json, **kwargs)

    def post_criteria(self, tender_id, acc_token, json, **kwargs):
        criteria_path = self.CRITERIA_COLLECTION_PATH.format(tender_id)
        path = self._get_api_path(criteria_path, acc_token=acc_token)
        return self.post(path, json, **kwargs)

    def get_bids(self, tender_id, **kwargs):
        bid_path = self.BIDS_COLLECTION_PATH.format(tender_id)
        path = self._get_api_path(bid_path)
        return self.get(path, **kwargs)

    def get_bid(self, tender_id, bid_id, acc_token, **kwargs):
        bid_path = self.BIDS_PATH.format(tender_id, bid_id)
        path = self._get_api_path(bid_path, acc_token=acc_token)
        return self.get(path, **kwargs)

    def post_bid(self, tender_id, json, **kwargs):
        bids_path = self.BIDS_COLLECTION_PATH.format(tender_id)
        path = self._get_api_path(bids_path)
        return self.post(path, json, **kwargs)

    def patch_bid(self, tender_id, bid_id, acc_token, json, **kwargs):
        bid_path = self.BIDS_PATH.format(tender_id, bid_id)
        path = self._get_api_path(bid_path, acc_token=acc_token)
        return self.patch(path, json, **kwargs)

    def post_bid_res(self, tender_id, bid_id, acc_token, json, **kwargs):
        bid_res_path = self.BIDS_RES_COLLECTION_PATH.format(tender_id, bid_id)
        path = self._get_api_path(bid_res_path, acc_token=acc_token)
        return self.post(path, json, **kwargs)

    def get_qualifications(self, tender_id, **kwargs):
        qualifications_path = self.QUALIFICATIONS_COLLECTION_PATH.format(tender_id)
        path = self._get_api_path(qualifications_path)
        return self.get(path, **kwargs)

    def get_qualification(self, tender_id, qualification_id, **kwargs):
        qualifications_path = self.QUALIFICATIONS_PATH.format(tender_id, qualification_id)
        path = self._get_api_path(qualifications_path)
        return self.get(path, **kwargs)

    def patch_qualification(self, tender_id, qualification_id, acc_token, json, **kwargs):
        qualifications_path = self.QUALIFICATIONS_PATH.format(tender_id, qualification_id, acc_token)
        path = self._get_api_path(qualifications_path, acc_token=acc_token)
        return self.patch(path, json, **kwargs)

    def get_awards(self, tender_id, **kwargs):
        awards_path = self.AWARDS_COLLECTION_PATH.format(tender_id)
        path = self._get_api_path(awards_path)
        return self.get(path, **kwargs)

    def get_award(self, tender_id, award_id, **kwargs):
        awards_path = self.AWARDS_PATH.format(tender_id, award_id)
        path = self._get_api_path(awards_path)
        return self.get(path, **kwargs)

    def post_award(self, tender_id, acc_token, json, **kwargs):
        awards_path = self.AWARDS_COLLECTION_PATH.format(tender_id)
        path = self._get_api_path(awards_path, acc_token=acc_token)
        return self.post(path, json, **kwargs)

    def patch_award(self, tender_id, award_id, acc_token, json, **kwargs):
        awards_path = self.AWARDS_PATH.format(tender_id, award_id, acc_token)
        path = self._get_api_path(awards_path, acc_token=acc_token)
        return self.patch(path, json, **kwargs)

    def get_contracts(self, tender_id, **kwargs):
        awards_path = self.CONTRACTS_COLLECTION_PATH.format(tender_id)
        path = self._get_api_path(awards_path)
        return self.get(path, **kwargs)

    def patch_contract(self, tender_id, contract_id, acc_token, json, **kwargs):
        awards_path = self.CONTRACTS_PATH.format(tender_id, contract_id, acc_token)
        path = self._get_api_path(awards_path, acc_token=acc_token)
        return self.patch(path, json, **kwargs)

    def get_agreements(self, tender_id, **kwargs):
        agreements_path = self.AGREEMENTS_COLLECTION_PATH.format(tender_id)
        path = self._get_api_path(agreements_path)
        return self.get(path, **kwargs)

    def patch_agreement(self, tender_id, agreement_id, acc_token, json, **kwargs):
        agreements_path = self.AGREEMENTS_PATH.format(tender_id, agreement_id, acc_token)
        path = self._get_api_path(agreements_path, acc_token=acc_token)
        return self.patch(path, json, **kwargs)

    def get_agreement_contracts(self, tender_id, agreement_id, **kwargs):
        agreement_contracts_path = self.AGREEMENT_CONTRACT_COLLECTION_PATH.format(tender_id, agreement_id)
        path = self._get_api_path(agreement_contracts_path)
        return self.get(path, **kwargs)

    def patch_agreement_contract(self, tender_id, agreement_id, contract_id, acc_token, json, **kwargs):
        agreement_contracts_path = self.AGREEMENT_CONTRACT_PATH.format(tender_id, agreement_id, contract_id, acc_token)
        path = self._get_api_path(agreement_contracts_path, acc_token=acc_token)
        return self.patch(path, json, **kwargs)

    def patch_credentials(self, tender_id, acc_token, json, **kwargs):
        credentials_path = self.CREDENTIALS_PATH.format(tender_id)
        path = self._get_api_path(credentials_path, acc_token=acc_token)
        return self.patch(path, json, **kwargs)


class AgreementsApiClient(BaseCDBClient):
    AGREEMENTS_PATH = "agreements/{}"

    def get_agreement(self, agreement_id, **kwargs):
        agreements_path = self.AGREEMENTS_PATH.format(agreement_id)
        path = self._get_api_path(agreements_path)
        return self.get(path, **kwargs)


class ContractsApiClient(BaseCDBClient):
    CONTRACTS_PATH = "contracts/{}"
    CREDENTIALS_PATH = "contracts/{}/credentials"

    def get_contract(self, contract_id, **kwargs):
        contracts_path = self.CONTRACTS_PATH.format(contract_id)
        path = self._get_api_path(contracts_path)
        return self.get(path, **kwargs)

    def patch_credentials(self, contract_id, acc_token, json, **kwargs):
        credentials_path = self.CREDENTIALS_PATH.format(contract_id)
        path = self._get_api_path(credentials_path, acc_token=acc_token)
        return self.patch(path, json, **kwargs)


class PlansApiClient(BaseCDBClient):
    PLANS_COLLECTION_PATH = "plans"
    PLANS_PATH = "plans/{}"
    TENDERS_COLLECTION_PATH = "plans/{}/tenders"

    def get_plan(self, plan_id, **kwargs):
        contracts_path = self.PLANS_PATH.format(plan_id)
        path = self._get_api_path(contracts_path)
        return self.get(path, **kwargs)

    def post_plan(self, json, **kwargs):
        tenders_path = self.PLANS_COLLECTION_PATH
        path = self._get_api_path(tenders_path)
        return self.post(path, json, **kwargs)

    def patch_plan(self, plan_id, acc_token, json, **kwargs):
        tenders_path = self.PLANS_COLLECTION_PATH.format(plan_id)
        path = self._get_api_path(tenders_path, acc_token=acc_token)
        return self.patch(path, json, **kwargs)

    def post_tender(self, plan_id, json, **kwargs):
        tenders_path = self.TENDERS_COLLECTION_PATH.format(plan_id)
        path = self._get_api_path(tenders_path)
        return self.post(path, json, **kwargs)


class DsApiClient(BaseApiClient):
    UPLOAD_PATH = "upload"
    HEADERS_DEFAULT = {}

    def __init__(self, host, username=None, password=None, session=None, **request_kwargs):
        super(DsApiClient, self).__init__(host, session=session, **request_kwargs)
        self._set_headers(request_kwargs, username, password)

    def _set_headers(self, request_kwargs, username, password):
        headers = self.HEADERS_DEFAULT
        headers.update(request_kwargs.pop("headers", {}))
        if username and password:
            headers.update({"Authorization": "Basic " + b64encode(
                "{}:{}".format(username, password).encode()
            ).decode()})
        request_kwargs.update(dict(headers=headers))
        self.kwargs.update(request_kwargs)

    def post_document_upload(self, files, **kwargs):
        path = self.UPLOAD_PATH
        return self.post(path, files=files, **kwargs)
