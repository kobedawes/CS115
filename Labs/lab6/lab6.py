'''
Created on 3/3/2022
@author:   Kobe Dawes
Pledge:    I pledge my honor that I have abided by the Stevens Honor System. Kobe Dawes

CS115 - Lab 6
'''

def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    
    if n%2 == 1:
        return True
    else: 
        return False

    
    #101010

    # an odd base-10 number will return a 1 for the least significant digit \
    # wheras an even base-10 nnumber will return a 0

    # when the least significant digit is dropped then integer division is done \
    # to the original value by the base meaning this can be seen with the values 10 and 11 \
    # both becomming 5 when they have gone throgh shifting

    # we would perform a left shift to the base-2 representation of Y. If the number is even this  would be enough. \
    # For odd numbers we would need to add 1 to the shifted number in the place of the least significat digit '1' \
    # we are able to do this because N = 2Y. And the muliplication of a binary number can be represented as a left shift


def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    if isOdd(n) is True:
        return numToBinary(n//2) + '1'
    else:
        return numToBinary(n//2) + '0'


def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    if s[-1] == '0':
        return  binaryToNum(s[:-1])*2
    else:
        return  binaryToNum(s[:-1])*2 + 1
  

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    num = binaryToNum(s) + 1
    biNum = numToBinary(num)
    if len(biNum) == len(s):
        return biNum

    elif s == "11111111":
        return "00000000"
    else:
        diff = len(s) -len(biNum)
        return '0'*diff + biNum
        
def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    if n >= 0:
        print(s)
        return count(increment(s), n-1)

"""the ternary representation of 59 is 2012. there are two 27s in 59 leaving a remainder or 5 \
    , zero 9s in 5, one 3 in 5 leaving a remainder of 2, and two 1s in 2
    
    alternatievely you can perform integer division with 3, and mark the least significant digit with the remainder of the division\
    59,19,6,2--> 2012 with the remainnder of 59//3 being 2, 19//3 being 1, 6//3 being 0, and 2//3 being 2
   """

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
   
    else:
        return numToTernary(n//3) + str(n%3)

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    if s[-1] == '0':
        return  ternaryToNum(s[:-1])*3
    elif s[-1] == '1':
        return  ternaryToNum(s[:-1])*3 + 1
    else:
        return ternaryToNum(s[:-1])*3 + 2


