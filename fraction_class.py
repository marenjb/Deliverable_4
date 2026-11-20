
class Fraction:
    """Represents a fraction."""

    def __init__(self, numerator: int, denominator: int) -> None:
        """Initialise the Fraction object."""

        # Controlling that the numerator is an integer
        if type(numerator) is not int:
            raise TypeError("Numerator must be an integer.")

        # Controlling that the denominator is an integer
        if type(denominator) is not int:
            raise TypeError("Denominator must be an integer.")

        # Controlling that the denominator is a positive number:
        if denominator <= 0:
            raise ValueError("Denominator must be greater than 0.")
        
        self._numerator = numerator
        self._denominator = denominator

    # Read-only properties for numerator and denominator
    @property
    def numerator(self) -> int:
        """Return the numerator."""
        return self._numerator

    @property
    def denominator(self) -> int:
        """Return the denominator."""
        return self._denominator

    # Special method 1: representing the object
    def __repr__(self) -> str:
        """Return a string representation of the fraction."""
        return f"Fraction({self.numerator}, {self.denominator})"

    # Special method 2: providing a human-readable string representation of the object
    def __str__(self) -> str:
        """Return a readable string representation of the fraction."""
        return f"{self.numerator}/{self.denominator}"

    # Special method 3: converting fraction to a float value
    def __float__(self) -> float:
        """Convert the fraction to a floating-point number."""
    
        # Dividing numerator by denominator to calculate
        return self.numerator / self.denominator
            
    # Equality comparison
    def __eq__(self, other: object) -> bool:
        """Check if two fractions are equal."""

        # Controlling that the object is a Fraction
        if not isinstance(other, Fraction):
            return NotImplemented

        # Use cross-multiplication to check equality
        return (
            self.numerator * other.denominator
            == other.numerator * self.denominator
        )

    # "Not equal" comparison
    def __ne__(self, other: object) -> bool:
        """Check if two fractions are not equal."""

        # Controlling that the object is a Fraction
        if not isinstance(other, Fraction):
            return NotImplemented

        # Using __eq__() to check if the fractions are equal
        # Not reverts the result
        return not self == other

    # "Less than" comparison
    def __lt__(self, other: object) -> bool:
        """Check if fraction is less than another fraction."""

        # Controlling that the object is a Fraction
        if not isinstance(other, Fraction):
            return NotImplemented

        # Using cross-multiplication again, this time with < rather than ==
        return(
            self.numerator * other.denominator
            < other.numerator * self.denominator
        )

    # "Less than or equal to" comparison
    def __le__(self, other: object) -> bool:
        """Check if fraction is less than or equal to another fraction."""

        # Controlling that the object is a Fraction
        if not isinstance(other, Fraction):
            return NotImplemented
       
        # Check if self is not greater than other
        return not (self > other)
    
    # "Greater than" comparison
    def __gt__(self, other: object) -> bool:
        """Check if fraction is greater than another fraction."""

        # Controlling that the object is a Fraction
        if not isinstance(other, Fraction):
            return NotImplemented

        # Reversing the comparison to check if self is greater than other
        return other < self

    # "Greater than or equal to" comparison
    def __ge__(self, other: object) -> bool:
        """Check if fraction is greater than or equal to another."""

        # Controlling that the object is a Fraction
        if not isinstance(other, Fraction):
            return NotImplemented

        # Check if self is not less than another
        return not self < other

    # Special method 4: adding two fractions
    def __add__(self, other: object) -> "Fraction":
        """Add two fractions and return a new fraction."""

        # Controlling that the object is a Fraction
        if not isinstance(other, Fraction):
            return NotImplemented

        # Calculate the numerator and denominator of the sum
        numerator = (
            self.numerator * other.denominator
            + other.numerator * self.denominator
        )

        denominator = self.denominator * other.denominator

        # Creating a new Fraction representing the sum
        return Fraction(numerator, denominator)
    