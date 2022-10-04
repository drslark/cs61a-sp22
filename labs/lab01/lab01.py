def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    factorial = 1
    while k > 0:
        factorial = factorial * n
        n = n - 1
        k = k - 1
    return factorial


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    quotient, reminder, summation = y, 0, 0
    while quotient > 0:
        quotient, reminder = quotient // 10, quotient % 10
        summation = summation + reminder
    return summation


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    quotient, reminder, is_prev_eight = n, 0, False
    while quotient > 0:
        quotient, reminder = quotient // 10, quotient % 10
        if reminder == 8 and is_prev_eight:
            return True
        if reminder == 8:
            is_prev_eight = True
        else:
            is_prev_eight = False
    return False
