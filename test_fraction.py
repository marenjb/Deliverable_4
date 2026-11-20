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

