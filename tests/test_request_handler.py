import unittest
from fake_webapp import EXAMPLE_APP
from nose.tools import assert_equals
from splinter.request_handler.request_handler import RequestHandler

class RequestHandlerTestCase(unittest.TestCase):
    def setUp(self):
        self.request = RequestHandler(EXAMPLE_APP)

    def test_should_receive_an_url_and_get_an_200_response(self):
        assert_equals(self.request.status_code, 200)

    def test_should_start_a_request_and_with_localhost_and_get_localhost_as_hostname(self):
        assert_equals(self.request.host, "localhost")