'''
CS 115, Lab 12, Inheritance

Author: Kobe Dawes
Pledge: I pledge my honor that I have abided by the stevens honor system. Kobe Dawes
'''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Part 1 
' Implement missing sections of the Car class.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Car(object):
    
    def __init__(self, make, model, mpg, tank_capacity):
        '''Write the constructor. It should take in four arguments:
        - make (a string, the company name, a.k.a. brand)
        - model (a string)
        - mpg (miles per gallon, a float)
        - tank_capacity (capacity of the gas tank in gallons, a float)
        These should all be assigned to corresponding private fields, i.e., with
        names that start with '__'.  Use the names in the 'str' method provided below.
        '''
        self.__make = str(make)
        self.__model = str(model)
        self.__mpg = mpg
        self.__TC = tank_capacity
    
    def get_make(self):
        """returns the make"""
        return self.__make

    def get_model(self):
        """returns the model"""
        return self.__model

    def get_mpg(self):
        """returns the mpg"""
        return self.__mpg

    def get_tank_capacity(self):
        """returns the tank capacity"""
        return self.__TC

   
    def set_make(self, newMake):
        """sets the make"""
        self.__make = newMake

    def set_model(self, newModel):
        """sets the model"""
        self.__model = newModel

    def set_mpg(self, newMPG):
        """sets the mpg"""
        self.__mpg = newMPG

    def set_tank_capacity(self, newTC):
        """sets the tank capacity"""
        self.__TC = newTC
        
    
    def get_total_range(self):
        '''Write a method called get_total_range.
        It returns the total distance the car can travel on a full tank of
        gas.'''
        range = self.__TC * self.__mpg
        return range


    def __str__(self):
        '''A string for printing information about a car.'''
        return self.__make + ' ' + self.__model + ', MPG: ' + str(self.__mpg) \
            + ', tank capacity: ' + str(self.__TC)



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Part 2 
' Implement missing sections of the HybridCar class. 
' Make HybridCar be a subclass of Car.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class HybridCar(Car):  
    
    def __init__(self, make, model, mpg, tank_capacity, battery_kwh, miles_per_kWh):
        '''Write the constructor. It should take in 6 arguments:
        - the first four are the same as in the Car constructor
        - battery_kWh (battery power in kilowatt-hours, a float)
        - miles_per_kWh (miles per kilowatt-hours, a float)
        The additional fields must be private.
        '''
        super().__init__(make, model, mpg, tank_capacity)
        self.__battery = battery_kwh
        self.__mpkwh = miles_per_kWh

    
    def get_battery_range(self):
        '''Returns the total distance the car can travel on a fully charged
        battery.
        '''
        battery_range = self.__battery * self.__mpkwh
        return battery_range

    def get_total_range(self):
        """Override the method get_total_range.
        Returns the total distance the car can travel on a full tank of
        gas and a fully charged battery.
        Do not do any math here except a single +. To get credit, you must call
        the methods you have already written."""
        total_range =  self.get_battery_range() + Car.get_total_range(self)
        return total_range

    def __str__(self):
        '''A string for printing information about a car.'''
        return super().__str__() + ', battery kWh: ' + \
            str(self.__battery) + ', miles/kWh: ' + \
            str(self.__mpkwh)
