import pytest
from unittest.mock import patch
from scraper import Login
import os
from io import StringIO
from scraper import ExitProgram


username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
    
def test_login_successful():
    # Mocking the input and getpass.getpass calls
    with patch('builtins.input', side_effect=[username]):
        with patch('getpass.getpass', side_effect=[password]):
            my_object = Login()
            assert my_object.login() == True

def test_login_failed():
    # Mocking the input and getpass.getpass calls
    with patch('builtins.input', side_effect=['invalid_username']):
        with patch('getpass.getpass', side_effect=['invalid_password']):
            my_object = Login()
            assert my_object.login() == False


class TestExitProgram:
    @patch('sys.exit')
    def test_exit(self, mock_exit):
        exit_program = ExitProgram()

        # Redirecting the standard output to a StringIO object
        with patch('sys.stdout', new_callable=StringIO) as fake_output:
            exit_program.exit()
            output = fake_output.getvalue()

        expected_output = "Exiting the program...\n"
        assert output == expected_output

        mock_exit.assert_called_with(0)
