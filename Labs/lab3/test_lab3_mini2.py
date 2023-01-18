'''
Created on Feb 8, 2015

@author: Brian Borowski

CS115 - Lab 3 Test Script
'''
import unittest
import lab3

class Test(unittest.TestCase):

    def test01(self):
        self.assertEqual(lab3.change(0, []), 0)

    def test02(self):
        self.assertEqual(lab3.change(1, []), float("inf"))

    def test03(self):
        self.assertEqual(lab3.change(1, [1, 5, 10]), 1)

    def test04(self):
        self.assertEqual(lab3.change(7, [1, 5, 10]), 3)

    def test05(self):
        self.assertEqual(lab3.change(29, [1, 5, 10, 20, 50, 100]), 6)

    def test06(self):
        self.assertEqual(lab3.change(29, [20, 29, 50]), 1)
        
    def test07(self):
        self.assertEqual(lab3.change(3, [2, 4, 5]), float("inf"))
        
    def test08(self):
        self.assertEqual(lab3.change(5, [0, 1, 2, 3]), 2)

    def test09(self):
        self.assertEqual(lab3.change(5, [0, -1, 1, 2, 3, 4]), 2)

    def test10(self):
        self.assertEqual(lab3.change(-1, [0, -1, 1, 2, 3, 4]), float("inf"))

    def test11(self):
        self.assertEqual(lab3.change(-1, [-1]), float("inf"))

if __name__ == "__main__":
    unittest.main()
