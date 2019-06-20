import people

from unittest.mock import *
from unittest import TestCase
from unittest import main


@patch('people.Person')
class MyTest(TestCase):

    def test_one(self, MockPerson):
        self.assertIs(people.Person, MockPerson)

    def test_two(self, MockSomeClass):
        self.assertIs(people.Person, MockSomeClass)

    def do_something(self):
        return 'something'


if __name__ == '__main__':
    main()
