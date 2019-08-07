import pytest
from programmer_day import ProgrammerDay

@pytest.fixture
def programmer_day(scope="module"):
    return ProgrammerDay()

def test_julian_year(programmer_day):
    pd = programmer_day
    # Year outside the range.
    assert pd.dayOfProgrammer(1699) == ''

def test_check_julian_leap_year(programmer_day):
    pd = programmer_day
    assert pd.is_julian_leap_year(1800) == True
    assert pd.is_julian_leap_year(1801) == False
    assert pd.is_julian_leap_year(1700) == True

def test_check_gregorian_leap_year(programmer_day):
    pd = programmer_day
    assert pd.is_gregorian_leap_year(1920) == True
    # Divisible by 400
    assert pd.is_gregorian_leap_year(2000) == True, 'Year 2000 is a Gregorian leap year.'
    # Divisible by 4 and divisible by 100
    assert pd.is_gregorian_leap_year(4100) == False, 'Year 4100 is not a Gregorian leap year.'

def test_transition_year(programmer_day):
    pd = programmer_day
    assert pd.dayOfProgrammer(1918) == '26.09.2018'

def test_gregorian_programmers_day(programmer_day):
    pd = programmer_day
    assert pd.dayOfProgrammer(2016) == '12.09.2016'
    assert pd.dayOfProgrammer(2017) == '13.09.2017'    
    assert pd.dayOfProgrammer(2100) == '13.09.2100'
    assert pd.dayOfProgrammer(2400) == '12.09.2400'

def test_julian_programmers_day(programmer_day):
    pd = programmer_day
    assert pd.dayOfProgrammer(1800) == '12.09.1800'
    assert pd.dayOfProgrammer(1705) == '13.09.1705'
    assert pd.dayOfProgrammer(1710) == '13.09.1710'