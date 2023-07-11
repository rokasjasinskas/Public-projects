import pytest
from jar import Jar

def test_jar_initialization():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

def test_jar_with_invalid_capacity():
    with pytest.raises(ValueError):
        jar = Jar(-5)
    with pytest.raises(ValueError):
        jar = Jar(3.5)

def test_jar_deposit():
    jar = Jar(10)
    jar.deposit(3)
    assert jar.size == 3

def test_jar_deposit_exceed_capacity():
    jar = Jar(5)
    with pytest.raises(ValueError):
        jar.deposit(6)

def test_jar_withdraw():
    jar = Jar(8)
    jar.deposit(4)
    jar.withdraw(2)
    assert jar.size == 2

def test_jar_withdraw_more_than_available():
    jar = Jar(6)
    jar.deposit(3)
    with pytest.raises(ValueError):
        jar.withdraw(5)

def test_jar_str_representation():
    jar = Jar(6)
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

if __name__ == '__main__':
    pytest.main()
