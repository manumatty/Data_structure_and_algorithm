#program to check given year is leap year or not
def is_leap_year(year):
    if (year%4 == 0 and year % 100 != 0) or year % 400 == 0:
        return "Leap Year"
    else:
        return "Not a Leap Year"
