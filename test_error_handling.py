import pytest
from main import is_leap_year

# Define test cases for leap years
leap_year_test_cases = [
    (2001, False),   # Divisible by 400
    (2003, True),   # Divisible by 4 but not by 100
]

# Create a test function to check leap years
@pytest.mark.parametrize("year, expected", leap_year_test_cases)
def test_leap_years(year, expected):
    try:
        print(f"Testing year: {year}")  # Print input year for debugging
        result = is_leap_year(year)
        assert result == expected, f"Year {year} should {'be' if expected else 'not be'} a leap year."
        print(f"Testing {year}: {'Pass' if result == expected else 'Fail'} - Expected: {expected}, Actual: {result}")
    except AssertionError as e:
        print(f"Assertion Error: {e}")
        # Handle the error here, if necessary

# Run the tests
if __name__ == "__main__":
    pytest.main()
