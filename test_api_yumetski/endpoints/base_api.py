import requests


class BaseAPI:
    def __init__(self, base_url):
        self.base_url: str = base_url
        self.base_headers: dict = {"Content-Type": "application/json"}
        self.response = None

    def _request(self, method: str, endpoint: str, headers: dict = None, **kwargs):
        url: str = f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"

        request_headers = self.base_headers.copy()

        if headers:
            request_headers.update(headers)

        self.response = requests.request(
            method=method,
            url=url,
            headers=request_headers,
            **kwargs
        )
        return self.response

    def get(self, endpoint: str, **kwargs):
        return self._request(method="GET", endpoint=endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs):
        return self._request(method="POST", endpoint=endpoint, **kwargs)

    def put(self, endpoint: str, **kwargs):
        return self._request(method="PUT", endpoint=endpoint, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self._request(method="DELETE", endpoint=endpoint, **kwargs)

    def patch(self, endpoint: str, **kwargs):
        return self._request(method="PATCH", endpoint=endpoint, **kwargs)
