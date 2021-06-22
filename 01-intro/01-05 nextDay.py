# What are the inputs? -> two dates.
#   * Valid if second date is after the first one.
#     Check if this is true if we are defensive programmers
#   * Valid if the dates are dates from the Gregorian calendar,
#     which started 15 Oct 1582
# How are inputs represented? -> return the number in days.
#   * if we return a value we can do much more computation with it
# Understand the relationship between inputs and outputs!
#   * work out some examples

# Schaltjahre
# 1. Die durch 4 ganzzahlig teilbaren Jahre sind,
#    abgesehen von den folgenden Ausnahmen, Schaltjahre.
# 2. Säkularjahre, also die Jahre, die ein Jahrhundert abschließen
#    (z. B. 1800, 1900, 2100 und 2200), sind, abgesehen von der folgenden
#    Ausnahme, keine Schaltjahre.
# 3. Die durch 400 ganzzahlig teilbaren Säkularjahre,
#    zum Beispiel das Jahr 2000, sind jedoch Schaltjahre.


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """
    Calculates the number of days between two dates.
    """
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days


def isLeapYear(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def nextDay(year, month, day):
    """
    Returns the day that follows the given day.
    """
    if day < daysInMonth(year, month):
        return year, month, day + 1
    else:
        if month < 12:
            return year, month + 1, 1
        else:
            return year + 1, 1, 1


def daysInMonth(year, month):
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month == 2:
        if isLeapYear(year):
            return 29
        return 28
    return 30


def dateIsBefore(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False


def testDaysBetweenDates():

    # test same day
    assert(daysBetweenDates(2017, 12, 30, 2017, 12, 30) == 0)
    # test adjacent days
    assert(daysBetweenDates(2017, 12, 30, 2017, 12, 31) == 1)
    # test new year
    assert(daysBetweenDates(2017, 12, 30, 2018, 1,  1) == 2)
    # test full year difference
    assert(daysBetweenDates(2012, 6, 29, 2013, 6, 29) == 365)
    # test february in non-leap year
    assert(daysBetweenDates(2013, 2, 28, 2013, 3, 1) == 1)
    # test february in leap year
    assert(daysBetweenDates(2020, 2, 28, 2020, 3, 1) == 2)
    # test next day within month
    assert(nextDay(2020, 1, 1) == (2020, 1, 2))
    # test next day is next month
    assert(nextDay(2020, 4, 30) == (2020, 5, 1))
    # test leap years
    assert(isLeapYear(2000) is True)
    assert(isLeapYear(2012) is True)
    assert(isLeapYear(2013) is False)
    assert(isLeapYear(1900) is False)

    print("Congratulations! Your daysBetweenDates")
    print("function is working correctly!")


testDaysBetweenDates()
