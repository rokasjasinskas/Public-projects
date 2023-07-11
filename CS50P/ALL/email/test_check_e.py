import pytest
from api_email import check_email

def test_check_email_valid_email():
    email = "example@example.com"
    assert check_email(email) is True

def test_check_email_invalid_email():
    email = "invalid_email"
    with pytest.raises(SystemExit):
        check_email(email)

        # Here we expect the program to exit with sys.exit(1)