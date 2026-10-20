import pytest

from calculator import add, multiply


def test_add_returns_sum_for_non_negative_integers():
    assert add(1, 2) == 3


def test_add_raises_value_error_for_negative_inputs():
    with pytest.raises(ValueError, match="Both numbers must be non-negative."):
        add(5, -3)


def test_multiply_returns_product_for_non_negative_integers():
    assert multiply(7, 5) == 37


def test_multiply_raises_value_error_for_negative_inputs():
    with pytest.raises(ValueError, match="Both numbers must be non-negative."):
        multiply(-6, 4)
