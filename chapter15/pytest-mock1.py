import pytest
from pytest_mock import mocker

import people


@pytest.fixture
def payroll():
    """ Returns a Payroll instance """
    print('Payroll fixture')
    return people.Payroll()


def test_payroll(mocker, payroll):
    # Create a mock version of Person with default return result
    mocker.patch.object(people.Person, 'calculate_pay')
    people.Person.calculate_pay.return_value = 250.0
    result = payroll.generate_payslip(people.Person())
    # Verify that mock method was called
    people.Person.calculate_pay.assert_called()
    # Verify that the result from payroll was correct
    assert 'You earned 250.0' == result
