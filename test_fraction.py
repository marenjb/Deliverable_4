# Importing the libraries and class
import pytest
from fraction_class import Fraction

# Creating test functions to be used in the ipynb-file

# Testing initialization and read-only properties
def test_initialization():
    """Test that fractions are correctly initiated."""

    # Creating a Fraction object
    f = Fraction(1,2)

    # Cheking the properties
    assert f.numerator == 1
    assert f.denominator == 2

    with pytest.raises(AttributeError):
        f.numerator = 3

    with pytest.raises(AttributeError):
        f.denominator = 4

# Testing if the validation check to ensure numerator and denominator are integers worked
def test_validation():
    """Test invalid numerator and denominator values."""

    # Testing a float value
    with pytest.raises(TypeError):
        Fraction(1.5,2)

    # Testing a string value
    with pytest.raises(TypeError):
        Fraction(1, "2")

    # Testing a boolean value
    with pytest.raises(TypeError):
        Fraction(True, 2)

    # Testing 0 as denominator
    with pytest.raises(ValueError):
        Fraction(1,0)

    # Testing a negative denominator
    with pytest.raises(ValueError):
        Fraction(1, -2)

# Testing all comparisons
def test_comparisons():
    """Test all six fraction comparisons."""

    # Creating test fractions
    f1 = Fraction(1,2)
    f2 = Fraction(2,4)
    f3 = Fraction(3,4)

    # Using assert to check
    assert f1 == f2
    assert f1 != f3
    assert f1 < f3
    assert f1 <= f2
    assert f3 > f1
    assert f3 >= f2

    # Testing False
    assert not (f1 == f3)
    assert not (f1 != f2)


# Testing representations
def test_representations():
    """Test string representations and float conversion."""

    # Creating a test fraction
    f = Fraction(1, 4)

    # Using assert to check
    assert repr(f) == "Fraction(1, 4)"
    assert str(f) == "1/4"
    assert float(f) == 0.25


# Testing the addition
def test_addition():

    # Creating test fractions
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 4)

    # Adding the fractions
    result = f1 + f2

    assert result == Fraction(3, 4)
    assert isinstance(result, Fraction)