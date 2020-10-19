import logging

import requests.adapters


DEFAULT_TIMEOUT = 60
DEFAULT_MAX_RETRIES = 10


class HTTPAdapter(requests.adapters.HTTPAdapter):

    def __init__(self, timeout=DEFAULT_TIMEOUT, max_reties=DEFAULT_MAX_RETRIES, *args, **kwargs):
        self.timeout = timeout
        super(HTTPAdapter, self).__init__(max_retries=max_reties, *args, **kwargs)

    def send(self, request, *args, **kwargs):
        kwargs['timeout'] = self.timeout
        logging.info("[{}] {}".format(request.method, request.url))
        return super(HTTPAdapter, self).send(request, *args, **kwargs)
