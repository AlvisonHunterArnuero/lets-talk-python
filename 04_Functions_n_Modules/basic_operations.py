def add(num1: int, num2: int) -> int:
    """
    Returns the sum of two numbers.

    Parameters:
        num1 (int): The first number.
        num2 (int): The second number.

    Returns:
        int: The sum of num1 and num2.
    """
    return num1 + num2


def subtract(num1: int, num2: int) -> int:
    """
    Returns the difference between two numbers.

    Parameters:
        num1 (int): The first number.
        num2 (int): The second number.

    Returns:
        int: The difference between num1 and num2.
    """
    return num1 - num2


def multiply(num1: int, num2: int) -> int:
    """
    Returns the product of two numbers.

    Parameters:
        num1 (int): The first number.
        num2 (int): The second number.

    Returns:
        int: The product of num1 and num2.
    """
    return num1 * num2


def division(num1: float, num2: float) -> float:
    """
    Returns the division of two numbers.

    Parameters:
        num1 (float): The numerator.
        num2 (float): The denominator.

    Returns:
        float: The result of num1 divided by num2.

    Raises:
        ZeroDivisionError: If num2 is zero.
    """
    if num2 == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return num1 / num2



