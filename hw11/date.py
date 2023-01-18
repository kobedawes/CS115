'''
Created on 4/27/22
@author:   Kobe Dawes
Pledge:    I pledge my honor that I have abided by Stevens Honor System. Kobe Dawes

CS115 - Hw 12 - Date class
'''
DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    def __repr__(self):
        '''This method also returns a string representation for the object.'''
        return self.__str__()

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False

    def copy(self):
        '''Returns a new object with the same month, day, year
        as the calling object (self).'''
        dnew = Date(self.month, self.day, self.year) 
        return dnew
    
    def equals(self, d2):
        '''Decides if self and d2 represent the same calendar date,
        whether or not they are the in the same place in memory.''' 
        return self.year == d2.year and self.month == d2.month and self.day == d2.day

    def tomorrow(self):
        """changes the self object to represent the next day"""
        DIM = [0,31,28,31,30,31,30,31,31,30,31,30,31]
        self.day += 1
        if self.isLeapYear() == True:
            DIM[2] += 1
        if self.day > DIM[self.month]:
            self.day = 1
            self.month += 1
        if self.month > 12:
            self.month = 1
            self.year += 1
    
    def yesterday(self):
        """changes the object to represent the day before"""
        DIM = [0,31,28,31,30,31,30,31,31,30,31,30,31]
        self.day -= 1
        if self.isLeapYear() == True:
            DIM[2] += 1
        if self.day <= 0:
            self.month -= 1
            self.day = DIM[self.month]
        if self.month <= 0:
            self.month = 12
            self.year -= 1
            if self.isLeapYear() == True:
                DIM[2] += 1
            self.day = DIM[self.month]
    
    def addNDays(self, N):
        """adds the indicated amount of days to the object"""
        for x in range(N):
            print(self)
            self.tomorrow()
        print(self)
            

    def subNDays(self, N):
        """subtracts the indicated amount of days to the object"""
        for x in range(N):
            print(self)
            self.yesterday()
        print(self)

    def isBefore(self, N):
        """checks whether the current date object is before the referenced  one"""
        if self.year < N.year:
            return True
        elif self.year == N.year and self.month < N.month: 
            return True
        elif self.year == N.year and self.month == N.month and self.day < N.day: 
            return True
        else:
            return False

    def isAfter(self, N):
        """checks whether the current date object is after the referenced  one"""
        if self.isBefore(N) == False and self.equals(N) == False:
            return True

        else:
            return False

    def diff(self, object):
        """returns the difference between the two dates in days"""
        count = 0
        newD = self.copy()
        if newD.isBefore(object) == True:
            while newD.isBefore(object) == True:
                newD.tomorrow()
                count -= 1
            return count
        else:
            while newD.isAfter(object) == True:
                newD.yesterday()
                count += 1
            return count

    def dow(self):
        """returns the day of the week indicated by the object"""

        DIW = ["Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday"]
       
        ref = Date(11, 9, 2011) #wednesday
        count = self.diff(ref)
        dayChange = count % 7
        return DIW[dayChange]

    