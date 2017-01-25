import pytest
import requests


@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    """ mocking get method with our code """
    monkeypatch.setattr(requests, "get", mock_api_call)


def mock_api_call(q, params, headers):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if "subreddits/search" in q:
        if params["q"] == "funny":
            return MockResponse({"data": {"children": [{'data': "arduino"}, {'data': "esp8266"}]}}, 200)
        if params["q"] == "a":
            return MockResponse({"data": {"children": []}}, 200)
    elif "r/" in q:
        if q.rsplit('/')[-2] == "DIY":
            return MockResponse({"data": {"children": [{'data': {"DIYch1": "", 'domain': ""}},
                                                       {'data': {"DIYch2": "", 'domain': ""}}]}}, 200)
        if q.rsplit('/')[-2] == "no_children":
            return MockResponse({"data": {"children": []}}, 200)
        if q.rsplit('/')[-2] == "no_domain":
            return MockResponse({"data": {"children": [{'data': {'DIYch1': "", 'domain': ""}},
                                                       {'data': {'DIYch2': ""}}]}}, 200)
    elif "comments/" in q:
        if "tesla" in q.rsplit('/')[-1]:
            return MockResponse([
                                {'data': {'children': [{'data': [1, 2]},
                                                       {'data': [3, 4]},
                                                       {'data': [5, 6]}]}}
                            ], 200)

    return MockResponse({}, 404)
