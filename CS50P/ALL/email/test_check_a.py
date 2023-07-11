import pytest
from api_email import check_APINAME



def test_check_APINAME_existing_api():
    api = "Trello"
    assert check_APINAME(api) == api

def test_check_APINAME_nonexistent_api():
    api = "NonexistentAPI"
    with pytest.raises(SystemExit):
        check_APINAME(api)

        # Here we expect the program to exit with sys.exit(1)
