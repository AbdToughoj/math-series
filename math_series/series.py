def fibonacci(n):
    """
    Return the (n) number in the Fibonacci sequence.
    param n: (int)
    return: (int)
    """
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    """
    Return the (n) number in the Fibonacci sequence.
    param n: (int)
    return: (int)
    """
    if n == 0:
        return 2
    elif n == 1:
        return 1

    return lucas(n - 1) + lucas(n - 2)


def sum_series(n, first=0, second=1):
    """
    Return the (n) number in a series defined by the given first two numbers.
    param n: (int)
    first: (int)
    second: (int)
    return: int
    """
    if n == 0:
        return first
    elif n == 1:
        return second
    else:
        return sum_series(n - 1, first, second) + sum_series(n - 2, first, second)
