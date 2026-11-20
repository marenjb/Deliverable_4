import pytest
from temperature_class import Temperature

# 1. Initialization test

def test_default_unit():
    """Test that Celsius is the default unit."""
    temp = Temperature(25)

    # Assert is used to test whether the statement is True
    # For example, here we test if the default unit is Celsius
    assert temp.unit == "C"
    assert temp.value == 25

def test_case_insensitive_units():
    """Test that lowercase units get converted to uppercase."""
    temp_c = Temperature(25, "c")
    temp_f = Temperature(80, "f")
    temp_k = Temperature(270, "k")

    assert temp_c.unit == "C"
    assert temp_f.unit == "F"
    assert temp_k.unit == "K"

def test_read_only():
    """Test that value and unit can not be modified directly."""
    temp = Temperature(25, "C")

    # Use pytest.raises(AttributeError) since we expect an error when
    # we try to modify the value or the unit
    # If Python gives this error, the test is passed
    with pytest.raises(AttributeError):
        temp.value = 30

    with pytest.raises(AttributeError):
        temp.unit = "F"

# 2. Validation

def test_invalid_units():
    """Test that invalid units raise ValueError."""
    invalid_units = ["X", "ABE", "", "", 123]

    # The loop goes thruough the list with invalid units and raises ValueError
    for unit in invalid_units:
        # This would give the ValueError defined in the Temperature class
        with pytest.raises(ValueError):
            Temperature(25, unit)

def test_below_absolute_zero():
    """Test that temperatures below absolute zero raise ValueError."""
    invalid_temperatures = [
        (-273.67, "C"),
        (-459.89, "F"),
        (-0.02, "K"),
    ]

    # Retrieve both value and unit to control if it is below absolute zero
    for value, unit in invalid_temperatures:
        with pytest.raises(ValueError):
            Temperature(value, unit)

# 4. Conversions

# Test absolute zero
def test_absolute_zero():
    """Test temperature conversions at absolute zero."""

    # Create a temperature object which represents -273,15 degrees Celsius
    temp = Temperature(-273.15, "C")

    # pytest.approx() indicate the result we would expect
    # Call the methods that converts the temperatures
    assert temp.to_celsius() == pytest.approx(-273.15)
    assert temp.to_fahrenheit() == pytest.approx(-459.67)
    assert temp.to_kelvin() == pytest.approx(0)

# Test Celsius-Fahrenheit crossover
def test_celsius_fahrenheit_crossover():
    """Test conversions at -40 degrees Celsius."""
    temp = Temperature(-40, "C")

    assert temp.to_celsius() == pytest.approx(-40)
    assert temp.to_fahrenheit() == pytest.approx(-40)
    assert temp.to_kelvin() == pytest.approx(233.15)

# Test freezing point of water
def test_freezing_point():
    """Test conversions at the freezing point of water."""
    temp = Temperature(0, "C")

    assert temp.to_celsius() == pytest.approx(0)
    assert temp.to_fahrenheit() == pytest.approx(32)
    assert temp.to_kelvin() == pytest.approx(273.15)

# Test human body temperature
def test_body_temperature():
    """Test conversions at human body temperature."""
    temp = Temperature(37, "C")

    assert temp.to_celsius() == pytest.approx(37)
    assert temp.to_fahrenheit() == pytest.approx(98.6)
    assert temp.to_kelvin() == pytest.approx(310.15)

# Test boiling point of water
def test_boiling_point():
    """Test conversions at the boiling point of water."""
    temp = Temperature(100, "C")

    assert temp.to_celsius() == pytest.approx(100)
    assert temp.to_fahrenheit() == pytest.approx(212)
    assert temp.to_kelvin() == pytest.approx(373.15)

