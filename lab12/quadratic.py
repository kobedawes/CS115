'''
Created on April 21 2022
Author:   Kobe Dawes
Pledge:    I pledge my honor that I have abided by the Stevens Honor System. Kobe Dawes

CS115 - Lab 12 - Quadratic Equation
'''

import math

class QuadraticEquation:

    def __init__(self, a, b, c): 
        if a == 0:
            raise ValueError("Coefficient 'a' cannot be 0 in a quadratic equation.")
            
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)

    def getA(self):
        """returns the value of a"""
        return self.a

    def getB(self):
        """returns the value of b"""
        return self.b

    def getC(self):
        """returns the value of c"""
        return self.c

    def discriminant(self):
        """finds the discriminant for the given variables"""
        a = self.getA()
        b = self.getB()
        c = self.getC()
        return b**2 - 4 * a * c
        

    def root1(self):
        """Computes root1"""
        
        dis = self.discriminant()
        a = self.getA()
        b = self.getB()
        c = self.getC()

        if dis < 0:
            return None
        return (-1*b + math.sqrt(dis)) / (2*a)

    def root2(self):
        """Computes root2"""
       
        dis = self.discriminant()
        a = self.getA()
        b = self.getB()
        c = self.getC()

        if dis < 0:
            return None
        return (-1*b - math.sqrt(dis)) / (2*a)
    
    def __str__(self):
        
        a = self.getA()
        b = self.getB()
        c = self.getC()

        if a > 0.0:
            if a == 1.0:
                checkA = "x^2 "
            else:
                checkA = str(a) + "x^2 "

        elif a < 0.0:
            if a == -1.0:
                checkA = "-x^2 "
            else:
                checkA = str(a) + "x^2 "

        if b > 0.0:
            if b == 1.0:
                checkB = "+ x "
            else:
                checkB = "+ " + str(b) + "x "

        elif b == 0.0:
            checkB = ""

        elif b < 0.0:
            if b == -1.0:
                checkB = "- x "
            else:
                checkB = "- " + str(b)[1:] + "x "

        if c > 0.0:
            checkC = "+ " + str(c) + " "

        elif c == 0.0:
            checkC = ""

        elif c < 0.0:
            checkC = "- " + str(c)[1:] + " "

        finalString = checkA + checkB + checkC + "= 0"
        
        return str(finalString)
    
