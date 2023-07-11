from datetime import date, timedelta
from unittest.mock import patch
import pytest
from seasons import birthday_date, date_minutes, convert_text


def test_birthday_date_valid_date():
    # Test valid date
    assert birthday_date("2023-06-03") == date(2023, 6, 3)


def test_birthday_date_invalid_date():
    # Test invalid date
    with pytest.raises(SystemExit) as exc_info:
        birthday_date("2023/06/03")

    assert str(exc_info.value) == "Invalid date"


def test_birthday_date_leap_year():
    # Test leap year
    assert birthday_date("2020-02-29") == date(2020, 2, 29)


def test_birthday_date_future_date():
    # Test future date
    today = date.today()
    future_date = date(today.year + 1, today.month, today.day)
    assert birthday_date(future_date.strftime("%Y-%m-%d")) == future_date


def test_date_minutes_zero_days():
    # Test zero days difference
    birthday = date.today()
    assert date_minutes(birthday) == 0


def test_date_minutes_one_day():
    # Test one day difference
    birthday = date.today() - timedelta(days=1)
    assert date_minutes(birthday) == 1440

def test_convert_text():
    assert convert_text(123456) == "One hundred and twenty-three thousand, four hundred and fifty-six"


if __name__ == "__main__":
    pytest.main()
