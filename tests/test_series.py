from math_series.series import fibonacci, lucas, sum_series

# # # ************* fibonacci tests***********************


def test_fibonacci_zero():
    """
    Base cases test
    """
    actual = fibonacci(0)
    expected = 0
    assert actual == expected


def test_fibonacci_one():
    """
    Base cases test
    """
    actual = fibonacci(1)
    expected = 1
    assert actual == expected


def test_fibonacci_four():
    """
    Small value test
    """
    actual = fibonacci(4)
    expected = 3
    assert actual == expected


def test_fibonacci_five():
    """
    Small value test
    """
    actual = fibonacci(5)
    expected = 5
    assert actual == expected


def test_fibonacci_twenty():
    """
    Large value test
    """
    actual = fibonacci(20)
    expected = 6765
    assert actual == expected


# ************* lucas tests***********************


def test_lucas_zero():
    """
    Base cases test
    """
    actual = lucas(0)
    expected = 2
    assert actual == expected


def test_lucas_one():
    """
    Base cases test
    """
    actual = lucas(1)
    expected = 1
    assert actual == expected


def test_lucas_four():
    """
    Small value test
    """
    actual = lucas(4)
    expected = 7
    assert actual == expected


def test_lucas_five():
    """
    Small value test
    """
    actual = lucas(5)
    expected = 11
    assert actual == expected


def test_lucas_ten():
    """
    Large value test
    """
    actual = lucas(10)
    expected = 123
    assert actual == expected


def test_lucas_twenty():
    """
    Large value test
    """
    actual = lucas(20)
    expected = 15127
    assert actual == expected


# ************* sum_series tests***********************


def test_sum_series_zero():
    """
    Base cases test
    """
    actual = sum_series(0)
    expected = 0
    assert actual == expected


def test_sum_series_one():
    """
    Base cases test
    """
    actual = sum_series(1)
    expected = 1
    assert actual == expected


def test_sum_series_four():
    """
    Small value test
    """
    actual = sum_series(4)
    expected = 3
    assert actual == expected


def test_sum_series_five():
    """
    Small value test
    """
    actual = sum_series(5)
    expected = 5
    assert actual == expected


def test_sum_series_three_values1():
    """
    Test with different starting values
    """
    actual = sum_series(5, 2, 3)
    expected = 21
    assert actual == expected


def test_sum_series_three_values2():
    """
    Test with different starting values
    """
    actual = sum_series(6, 2, 3)
    expected = 34
    assert actual == expected


def test_sum_series_twenty():
    """
    Large value test
    """
    actual = sum_series(20)
    expected = 6765
    assert actual == expected
