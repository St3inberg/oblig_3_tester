def is_leap_year(year):
    """
    Check if a year is a leap year according to the Gregorian calendar rules.

    :param year: The year to check.
    :return: True if it's a leap year, False otherwise.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False



