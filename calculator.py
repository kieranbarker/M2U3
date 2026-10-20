def add(a, b):
    """Returns the sum of two non-negative numbers."""
    if a < 0 or b < 0:
        raise ValueError("Both numbers must be non-negative.")
    return a + b


def multiply(a, b):
    if a < 0 or b < 0:
        raise ValueError("Both numbers must be non-negative.")
    return a * b
