import math


class Temperature:
    """Represent a temperature in Celsius (C), Fahrenheit (F) or Kelvin (K)."""

    def __init__(self, value: float, unit: str) -> None:
        """Initialises a Temperature object."""

        # Control that the unit is a string and 
        if not isinstance(unit, str) or unit.upper() not in ("C", "F", "K"):
            raise ValueError("Unit must be C, F or K.")

        self._value = float(value)
        # Use upper() to make all letters in big case
        self._unit = unit.upper()

        # Checks that the temperature is not below zero Kelvin
        if self.to_kelvin() < 0 and not math.isclose(
            self.to_kelvin(), 0.0, rel_tol=0.0, abs_tol=1e-9
        ):
            raise ValueError("Temperature cannot be below zero Kelvin.")

    # Make value and unit attributes read-only
    @property
    def value(self) -> float:
        """Return the temperature value."""
        return self._value

    @property
    def unit(self) -> str:
        """Return the unit."""
        return self._unit

    # Three converting methods is created by the same principle
    # Using if, elif and else to controll the unit of the temperature
    def to_celsius(self) -> float:
        """Convert the temperature to Celsius."""

        # If the temperature is in Celsius, return the value 
        if self.unit == "C":
            return self.value
        # If the temperature is in Fahrenheit, use the fahrenheit formula
        elif self.unit == "F":
            return (self.value -32) * 5 / 9
        # If the temperature is in Kelvin, use the kelvin formula
        else:
            return self.value - 273.15

    # The two next methods use the same principle, but with other formulas
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

    # Creates a method that use the converting methods created, to make a new object
    def convert_to(self, target_unit: str) -> "Temperature":
        """Return a new temperature object in the target unit."""

        # Controls that the gived target unit is valid
        if not isinstance(target_unit, str):
            raise ValueError("Target unit must be C, F or K")

        target_unit = target_unit.upper()

        # Converting the temperature to the target unit
        if target_unit == "C":
            new_value = self.to_celsius()
        elif target_unit == "F":
            new_value = self.to_fahrenheit()
        elif target_unit == "K":
            new_value = self.to_kelvin()
        else:
            raise ValueError("Target unit must be C, F or K.")

        # Creating a new object calling Temperature()
        return Temperature(new_value, target_unit)

    def __repr__(self) -> str:
        """Return a string representation of the temperature."""
        return f"Temperature({self.value}, '{self.unit}')"

    def __str__(self) -> str:
        """Return a more readable string representation of the temperature."""
        # Creating a dictionary to get the correct symbol based on the unit
        unit_symbols = {"C": "°C", "F": "°F", "K": "K"}
        return f"{self.value:.2f} {unit_symbols[self.unit]}"

    # Create a help function to make it easier to compare temperatures with different units
    def _compare_value(self, other: "Temperature") -> tuple[float, float]:
        """Return both temperatures converted to Celsius."""
        return self.to_celsius(), other.to_celsius()

    # Checks if the object we compare with is equal to self
    def __eq__(self, other: object) -> bool:
        # Use isinstance() to control that the object is an instance of Temperature
        if not isinstance(other, Temperature):
            # If it is not an instance return NotImplemented
            return NotImplemented

        a, b = self._compare_value(other)
        return math.isclose(a, b, rel_tol=0.0, abs_tol=1e-9)

    # Checks if the object we compare with is not equal to self
    def __ne__(self, other: object) -> bool: 
        if not isinstance(other, Temperature):
            return NotImplemented

        return not self == other

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Temperature):
            return NotImplemented

        a, b = self._compare_value(other)
        return a < b and not math.isclose(a, b, rel_tol=0.0, abs_tol=1e-9)

    def __le__(self, other: object) -> bool:
        if not isinstance(other, Temperature):
            return NotImplemented

        a, b = self._compare_value(other)
        return a < b or math.isclose(a, b, rel_tol=0.0, abs_tol=1e-9)

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Temperature):
            return NotImplemented

        a, b = self._compare_value(other)
        return a > b and not math.isclose(a, b, rel_tol=0.0, abs_tol=1e-9)
    
    def __ge__(self, other: object) -> bool:
        if not isinstance(other, Temperature):
            return NotImplemented

        a, b = self._compare_value(other)
        return a > b or math.isclose(a, b, rel_tol=0.0, abs_tol=1e-9)

