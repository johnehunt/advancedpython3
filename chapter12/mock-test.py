import external_module

from unittest.mock import *

from unittest import TestCase
from unittest import main
import json


def some_func():
    # Calls out to external API - whcih we want to mock
    response = external_module.api_call()
    return response


class test_some_func_calling_api(TestCase):

    @patch('external_module.api_call')
    def test_some_func(self, mock_api_call):
        # Sets up mock version of api_call
        mock_api_call.return_value = MagicMock(status_code=200, response=json.dumps({'key': 'value'}))
        # Calls some_func(0 that calls the (mock) api_call() function
        result = some_func()
        print('result.response:', result.response)
        # Check that the result returned from some_func() is what was expected
        self.assertEqual(result.status_code, 200, "returned status code is not 200")
        self.assertEquals(result.response, '{"key": "value"}', "response JSON incorrect")


if __name__ == '__main__':
    main()
