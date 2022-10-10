"""Test cases for Karatsuba multiplication."""

import pytest

from src.course1.week1.karatsuba import multiply


def test_karatsuba_1_2():
    """Test Karatsuba Multiplication 1x2"""
    assert multiply(1, 2) == 2


def test_karatsuba_12_34():
    """Test Karatsuba Multiplication 12x34"""
    assert multiply(12, 34) == 408


def test_karatsuba_123_456():
    """Test Karatsuba Multiplication 123x456"""
    assert multiply(123, 456) == 56088


def test_karatsuba_1234_5678():
    """Test Karatsuba Multiplication 1234x5678"""
    assert multiply(1234, 5678) == 7006652


def test_karatsuba_big_integers():
    """Test Karatsuba Multiplication 64-digit Integers"""
    x = 3141592653589793238462643383279502884197169399375105820974944592
    y = 2718281828459045235360287471352662497757247093699959574966967627
    expected = 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184  # pylint: disable=locally-disabled, line-too-long
    assert multiply(x, y) == expected


def test_karatsuba_different_size():
    """Test Karatsuba Multiplication Different Size Integers"""
    assert multiply(1234567, 890) == 1098764630


def test_karatsuba_zero():
    """Test Karatsuba Multiplication Zero Integer"""
    assert multiply(0, 1234567890) == 0


def test_karatsuba_negative_integer():
    """Test Karatsuba Multiplication Negative Integer"""
    with pytest.raises(ValueError):
        multiply(-1, 1)
