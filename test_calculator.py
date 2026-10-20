import pytest

from calculator import add


def test_add_returns_sum_for_non_negative_integers():
    assert add(1, 2) == 3


def test_add_raises_value_error_for_negative_inputs():
    with pytest.raises(ValueError, match="Both numbers must be non-negative."):
        add(5, -3)
