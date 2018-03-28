import hashlib
import hmac
import json
import time
import urllib.parse

import requests

from config import config


class Client(object):
    api = config.get("api")
    base_url = config.get("base_url")

    @classmethod
    def sign(cls, parts):

        api_key = cls.api.get("secret").encode()
        return hmac.new(api_key, parts.encode(), hashlib.sha256).hexdigest()

    @classmethod
    def get_signed_url(cls, req_method, path, params=None, json_data=None):
        sign_params = {"api_key": cls.api.get("key"),
                       "api_timestamp": int(time.time())}
        if params:
            sign_params.update(params)
        parts = [req_method, path, urllib.parse.urlencode(sign_params)]
        if json_data:
            parts.append(json.dumps(json_data))

        signature = cls.sign("&".join(parts))
        sign_params["api_signature"] = signature
        return "".join([path, "?", urllib.parse.urlencode(sign_params)])

    @classmethod
    def send(cls, method, path, params=None, json_data=None):
        signed_url = urllib.parse.urljoin(
            cls.base_url,
            cls.get_signed_url(method.upper(), path, params, json_data)
        )
        res = requests.request(method, signed_url, params=params,
                               json=json_data)
        res.raise_for_status()
        return res
