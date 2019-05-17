from unittest.mock import *

from unittest import TestCase
from unittest import main

class SomeClass():

    def _hidden_method(self):
        return 0

    def public_method(self, x):
        return self._hidden_method() + x

class test_SomeClass_public_interface(TestCase):

    def test_public_method(self):
        test_object = SomeClass()
        # Set up canned response on mock method
        test_object._hidden_method = MagicMock(name = 'hidden_method')
        test_object._hidden_method.return_value = 10
        # Test the object
        result = test_object.public_method(5)
        self.assertEqual(15, result, 'return value from public_method incorrect')

if __name__ == '__main__':
    main()