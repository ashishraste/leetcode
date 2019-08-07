target_year_period = [1700, 2700]
julian_years = [1700, 1917]
gregorian_years = [1919, 2700]
transition_year = 1918

class ProgrammerDay(object):
    def __init__(self):
        pass    

    def is_gregorian_leap_year(self, year: int) -> bool:
        ''' Gregorian leap years are (divisible by 4 and not divisible by 100) OR (divisible by 400).'''
        return True if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0) else False

    def is_julian_leap_year(self, year: int) -> bool:
        ''' Julian leap years are divisible by 4 in a Julian year.'''
        return True if year % 4 == 0 else False

    def dayOfProgrammer(self, year: int) -> str:
        if not (target_year_period[0] <= year <= target_year_period[1]):
            return ''

        if year == transition_year:
            return '26.09.2018'

        def leap_programmer_day(year):
            return '12.09.%s' % year
        
        def non_leap_programmer_day(year):
            return '13.09.%s' % year
        
        if year <= julian_years[1]:
            return leap_programmer_day(year) if self.is_julian_leap_year(year) else non_leap_programmer_day(year)
        elif year >= gregorian_years[0]:
            return leap_programmer_day(year) if self.is_gregorian_leap_year(year) else non_leap_programmer_day(year)