import pytest
from main import is_leap_year

# Define a parametrized fixture for years
@pytest.fixture(params=[2000, 2004, 2028])
def leap_years(request):
    return request.param

# Test function that uses the leap_years fixture to check if it's a leap year
def test_leap_years(leap_years):
    result = is_leap_year(leap_years)
    assert result == True, f"Year {leap_years} should be a leap year."

# Entry point of the script: if this script is run directly, execute the tests using pytest
if __name__ == "__main__":
    pytest.main()
