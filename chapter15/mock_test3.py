import external_module

from unittest.mock import *

from unittest import TestCase
from unittest import main
import json


def some_func():
    # Calls out to external API - which we want to mock
    response = external_module.api_call()
    return response


def some_func_with_param(param):
    # call out to api module
    response = external_module.api_call_with_param(param)
    return response


class test_some_func_calling_api(TestCase):

    @patch('external_module.api_call')
    def test_some_func(self, mock_api_call):
        # Sets up mock version of api_call
        mock_api_call.return_value = MagicMock(status_code=200, response=json.dumps({'key': 'value'}))
        # Calls some_func() that calls the (mock) api_call() function
        result = some_func()
        # Check that the result returned from some_func() is what was expected
        self.assertEqual(result.status_code, 200, "returned status code is not 200")
        self.assertEqual(result.response, '{"key": "value"}', "response JSON incorrect")

    @patch('external_module.api_call_with_param')
    def test_some_func_with_param(self, mock_api_call):
        # Sets up mock version of api_call
        mock_api_call.return_value = MagicMock(status_code=200, response=json.dumps({'age': '23'}))
        result = some_func_with_param('Phoebe')
        # Check that the result returned from some_func() is what was expected
        self.assertEqual(result.response, '{age": "23"}', 'JSON result incorrect')
        # Verify that the mock_api_call was called with the correct params
        mock_api_call.api_call_with_param.assert_called_with('Phoebe')


if __name__ == '__main__':
    main()
