import math

# Define the Temperature class
class Temperature:
    """Represent a temperature in Celsius (C), Fahrenheit (F) or Kelvin (K)."""

    def __init__(self, value: float, unit: str = "C") -> None:
        """Initialises a Temperature object."""

        # Checks if the unit is a string and has one of the defined temperature units
        if not isinstance(unit, str) or unit.upper() not in ("C", "F", "K"):
            raise ValueError("Unit must be C, F or K.")

        self._value = float(value)
        # Convert the unit to uppercase to be able to handle lowercase input
        self._unit = unit.upper()

        # Check that the temperature is not below absolute zero
        kelvin = self.to_kelvin()
        if self.to_kelvin() < 0 and not math.isclose(
            self.to_kelvin(), 0.0, rel_tol=0.0, abs_tol=1e-9
        ):
            raise ValueError("Temperature cannot be below absolute zero.")

    # Make the value and unit attributes read-only
    @property
    def value(self) -> float:
        """Return the temperature value."""
        return self._value

    @property
    def unit(self) -> str:
        """Return the unit."""
        return self._unit

    # The three conversion methods follow the same principle
    # Using if, elif and else statements to check the temperature unit
    def to_celsius(self) -> float:
        """Convert the temperature to Celsius."""

        # If the temperature is already in Celsius, return its value 
        if self.unit == "C":
            return self.value
        # If the temperature is in Fahrenheit, use the Fahrenheit formula
        elif self.unit == "F":
            return (self.value -32) * 5 / 9
        # If the temperature is in Kelvin, use the kelvin conversion formula
        else:
            return self.value - 273.15

    # The two next methods use the same principle, but use different formulas
    def to_fahrenheit(self) -> float:
        """Convert the temperature to Fahrenheit."""
        if self.unit == "F":
            return self.value
        elif self.unit == "C":
            return self.value * 9 / 5 + 32
        else:
            return (self.value - 273.15) * 9 / 5 + 32

    def to_kelvin(self) -> float:
        """Convert the temperature to Kelvin."""
        if self.unit == "K":
            return self.value
        elif self.unit == "C":
            return self.value + 273.15
        else:
            return (self.value -32) * 5 / 9 + 273.15

    # Create a method that uses the conversion methods to create a new object
    def convert_to(self, target_unit: str) -> "Temperature":
        """Return a new temperature object in the target unit."""

        # Check that the target unit is a string
        if not isinstance(target_unit, str):
            raise ValueError("Target unit must be C, F or K")

        target_unit = target_unit.upper()

        # Convert the temperature to the target unit
        if target_unit == "C":
            new_value = self.to_celsius()
        elif target_unit == "F":
            new_value = self.to_fahrenheit()
        elif target_unit == "K":
            new_value = self.to_kelvin()
        else:
            raise ValueError("Target unit must be C, F or K.")

        # Create and return a new Temperature object calling Temperature()
        return Temperature(new_value, target_unit)

    def __repr__(self) -> str:
        """Return a string representation of the temperature."""
        return f"Temperature({self.value}, '{self.unit}')"

    def __str__(self) -> str:
        """Return a more readable string representation of the temperature."""
        # Map each unit to its corresponding symbol
        unit_symbols = {"C": "°C", "F": "°F", "K": "K"}
        return f"{self.value:.2f} {unit_symbols[self.unit]}"

    # Create a helper method to make it easier to compare temperatures with different units
    def _compare_value(self, other: "Temperature") -> tuple[float, float]:
        """Return both temperatures converted to Celsius."""
        return self.to_celsius(), other.to_celsius()

    # Check whether the other object represents the same temperature as self
    def __eq__(self, other: object) -> bool:
        """Check whether two temperatures are equal."""
        # Use isinstance() to check whether the object is a Temperature instance
        if not isinstance(other, Temperature):
            # Return NotImplemented if the other object is not a Temperature instance
            return NotImplemented

        a, b = self._compare_value(other)
        return math.isclose(a, b, rel_tol=0.0, abs_tol=1e-9)

    # Check whether the other object represents a different temperature from self
    def __ne__(self, other: object) -> bool:
        """Check wheter two temperatures are not equal.""" 
        if not isinstance(other, Temperature):
            return NotImplemented

        # Use the equality method but return the opposite result
        return not self == other

    # Check whether self represents a lower temperature than the other object
    def __lt__(self, other: object) -> bool:
        """Check whether self is less than the other temperature."""
        if not isinstance(other, Temperature):
            return NotImplemented

        a, b = self._compare_value(other)
        # Check that self is lower and that the values are not equal
        return a < b and not math.isclose(a, b, rel_tol=0.0, abs_tol=1e-9)

    # Check whether self represents a lower or equal temperature
    def __le__(self, other: object) -> bool:
        """Check whether self is less than or equal to the other temperature."""
        if not isinstance(other, Temperature):
            return NotImplemented

        a, b = self._compare_value(other)
        # Return True is self is lower or if the values are equal
        return a < b or math.isclose(a, b, rel_tol=0.0, abs_tol=1e-9)

    # Check whether self represents a higher temperature than the other object
    def __gt__(self, other: object) -> bool:
        """Check whether self is greater than the other temperature."""
        if not isinstance(other, Temperature):
            return NotImplemented

        a, b = self._compare_value(other)
        return a > b and not math.isclose(a, b, rel_tol=0.0, abs_tol=1e-9)

    # Check whether self represents a higher or equal temperature
    def __ge__(self, other: object) -> bool:
        """Check whether self is greater than or equal to the other temperature."""
        if not isinstance(other, Temperature):
            return NotImplemented

        a, b = self._compare_value(other)
        return a > b or math.isclose(a, b, rel_tol=0.0, abs_tol=1e-9)

