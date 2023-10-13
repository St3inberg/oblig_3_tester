import pytest
from main import is_leap_year

# Define test cases for non-leap years
non_leap_year_test_cases = [
    (1700, False),  # Divisible by 4 and 100 but not by 400
    (1800, False),  # Divisible by 4 and 100 but not by 400
    (1900, False),  # Divisible by 4 and 100 but not by 400

]

# Create a test function to check non-leap years
@pytest.mark.parametrize("year, expected", non_leap_year_test_cases)
def test_non_leap_years(year, expected):
    # Call the is_leap_year function with the current year and get the result
    result = is_leap_year(year)
    # Print the test result
    print(f"Testing {year}: {'Pass' if result == expected else 'Fail'} - Expected: {expected}, Actual: {result}")

# Entry point of the script: if this script is run directly, execute the tests using pytest
if __name__ == "__main__":
    pytest.main()
