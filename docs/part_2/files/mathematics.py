######## MODULE: mathematics ########

## Mathematics contains functions with mathematical operations are used to perform various mathematical operations,
## such as finding the roots of an equation, exponentiation, multiplication and division.
## about Sphinx documentation – https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html


def square_root(val: int) -> float:
    """
    The function returns the square root of the number.
    
    :param val: a number from an integer set
    :type val: int
    
    :return: squre root of val
    :rtype: float
    """
    return val ** .5


def multiply(val: int, oth_val: int) -> int:
    """
    The function returns the product of two numbers.
    
    :param val: a number from an integer set
    :type val: int

    :param oth_val: other number from an integer set
    :type val: int

    :return: the product of two numbers
    :rtype: int
    """
    return sum([val for i in range(oth_val)])


def divide(val: int, oth_val: int) -> int:
    """
    The function returns the quotient of two numbers.
    
    :param val: a number from an integer set
    :type val: int

    :param oth_val: other number from an integer set
    :type val: int

    :return: the quotient of two numbers
    :rtype: int
    """
    int_div = 0
    
    while val > 0:
        val -= oth_val
        int_div += 1
            
    return int_div


def pow(val: int, p: int) -> int:
    """
    The function returns the power of a number.
    
    :param val: base – a number from an integer set
    :type val: int
    :param p: power to which the number is raised
    :type val: int
    :return: a number raised to a power
    :rtype: int

    """
    res = 1
    for i in range(1, p+1):
        res = multiply(val, res)

    return res 




