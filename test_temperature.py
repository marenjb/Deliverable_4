import pytest
from temperature_class import Temperature

# 1. Initialization test

# Every function name starts with test_, since
# Pytest recognizes functions that start with test_
def test_default_unit():
    """Test that Celsius is the default unit."""
    # We create a temperature object without defining the unit
    temp = Temperature(25)

    # Assert is used to check whether a condition is True
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
    # The test passes if the expected AttributeError is raised
    with pytest.raises(AttributeError):
        temp.value = 30

    with pytest.raises(AttributeError):
        temp.unit = "F"


# 2. Validation

def test_invalid_units():
    """Test that invalid units raise ValueError."""
    invalid_units = ["X", "ABE", "", 123]

    # Test that each invalid unit raises a ValueError
    for unit in invalid_units:
        # Expect the ValueError defined in the Temperature class
        with pytest.raises(ValueError):
            Temperature(25, unit)


def test_below_absolute_zero():
    """Test that temperatures below absolute zero raise ValueError."""
    invalid_temperatures = [
        (-273.67, "C"),
        (-459.89, "F"),
        (-0.02, "K"),
    ]

    # Unpack each temperature value and unit to test validation
    for value, unit in invalid_temperatures:
        with pytest.raises(ValueError):
            Temperature(value, unit)


# 3. Conversions

# Test absolute zero
def test_absolute_zero():
    """Test temperature conversions at absolute zero."""

    # Create a temperature object which represents -273.15 degrees Celsius
    temp = Temperature(-273.15, "C")

    # Use pytest.approx() to allow small floating-point differnces
    # Call the conversion methods defined in the Temperature class
    assert temp.to_celsius() == pytest.approx(-273.15)
    assert temp.to_fahrenheit() == pytest.approx(-459.67)
    assert temp.to_kelvin() == pytest.approx(0)

# Test Celsius-Fahrenheit crossover
def test_celsius_fahrenheit_crossover():
    """Test conversions at -40 degrees Celsius."""
    temp = Temperature(-40, "F")

    assert temp.to_celsius() == pytest.approx(-40)
    assert temp.to_fahrenheit() == pytest.approx(-40)
    assert temp.to_kelvin() == pytest.approx(233.15)

# Test freezing point of water
def test_freezing_point():
    """Test conversions at the freezing point of water."""
    temp = Temperature(273.15, "K")

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
    temp = Temperature(212, "F")

    assert temp.to_celsius() == pytest.approx(100)
    assert temp.to_fahrenheit() == pytest.approx(212)
    assert temp.to_kelvin() == pytest.approx(373.15)


# 4. Round-trip conversions

def test_round_trip():
    """Test that round-trip conversions reproduce the originale temperature."""

    # Create a start temperature with "C" as unit
    original = Temperature(20, "C")

    # Use the convert_to() method from Temperature class
    fahrenheit = original.convert_to("F")
    kelvin = fahrenheit.convert_to("K")
    celsius = kelvin.convert_to("C")

    # Check that the converted value and unit match the original
    assert celsius.value == pytest.approx(original.value)
    assert celsius.unit == original.unit
    assert celsius == original


# 5. Cross-unit comparisons

def test_cross_unit_comparisons():
    """Test equality and ordering across mixed units."""

    # Create three temperature objects to be compared
    temp_c = Temperature(0, "C")  # 0 degrees Celsius
    temp_f = Temperature(32, "F")  # 0 degrees Celsius
    temp_k = Temperature(373.15, "K")  # 100 degrees Celsius

    # Test equality
    assert temp_c == temp_f

    # Test inequality
    assert temp_c != temp_k

    # Test less than
    assert temp_c < temp_k

    # Test less than or equal to
    assert temp_c <= temp_k

    # Test greater than
    assert temp_k > temp_c

    # Test greater than or equal to
    assert temp_k >= temp_c

    # Test that comparisons expected to be False return False
    assert not (temp_c == temp_k)
    assert not (temp_k < temp_c)
    assert not (temp_c > temp_f)


# 6. Formatting

def test_repr():
    """Test the string representation of the temperature object."""
    temp = Temperature(25, "C")

    assert repr(temp) == "Temperature(25.0, 'C')"


def test_str():
    """Test the readable string representation."""
    temp = Temperature(25, "C")

    assert str(temp) == "25.00 °C"

