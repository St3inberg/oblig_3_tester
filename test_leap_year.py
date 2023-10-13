from main import is_leap_year

# Define test cases as a list of tuples, where each tuple contains a year and the expected leap year status
leap_year_test_cases = [
    (2000, True),  # Divisible by 400 - Leap Year
    (2004, True),  # Divisible by 4 - Leap Year
    (2008, True),  # Divisible by 4 - Leap Year
    (2012, True),  # Divisible by 4 - Leap Year
    (2016, True),  # Divisible by 4 - Leap Year
    (2020, True),  # Divisible by 4 but not by 100 - Leap Year
    (2024, True),  # Divisible by 4 - Leap Year
    (2028, True),  # Divisible by 4 - Leap Year
    (2032, True),  # Divisible by 4 - Leap Year
]

# Create a test function with a descriptive name
def test_leap_years():
    # Iterate over each test case
    for year, is_leap_year_expected in leap_year_test_cases:
        # Call the is_leap_year function with the current year and get the result
        is_leap_year_result = is_leap_year(year)
        # Use assert to check if the result matches the expected value
        assert is_leap_year_result == is_leap_year_expected, f"Year {year} should {'be' if is_leap_year_expected else 'not be'} a leap year. Got: {is_leap_year_result}"

# Entry point of the script: if this script is run directly, execute the test function
if __name__ == "__main__":
    test_leap_years()

