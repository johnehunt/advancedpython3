from unittest.mock import *

from unittest import TestCase
from unittest import main

class SomeClass():

    def _hidden_method(self):
        return 0

    def public_method(self, x):
        return self._hidden_method() + x

class test_SomeClass_public_interface(TestCase):

    @patch.object(SomeClass, '_hidden_method')
    def test_public_method(self, mock_method):
        # Set up canned response
        mock_method.return_value = 10
        # Create object to be tested
        test_object = SomeClass()
        result = test_object.public_method(5)
        self.assertEqual(15, result, 'return value from public_method incorrect')

if __name__ == '__main__':
    main()
