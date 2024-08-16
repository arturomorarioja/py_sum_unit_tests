from app.calculator import sum_numbers

#
# Positive testing
#
def test_add_4_to_13_is_17():
    # Arrange
    number_1 = 4
    number_2 = 13
    expected = 17

    # Act
    result = sum_numbers(number_1, number_2)

    # Assert
    assert result == expected

def test_add_15_to_21_is_36():
    # Arrange, Act and Assert in one line
    assert sum_numbers(15, 21) == 36

def test_add_minus_4_to_5_is_1():
    assert sum_numbers(-4, 5) == 1

#
# Negative testing
#
def test_add_1_to_1_is_not_1():
    assert not sum_numbers(1, 1) == 1

#
# Data type testing
#
def test_add_two_numbers_returns_a_number():
    assert isinstance(sum_numbers(4, 5), (int, float))

def test_add_two_integers_returns_an_integer():
    assert isinstance(sum_numbers(4, 5), int)