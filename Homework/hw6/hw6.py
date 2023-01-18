'''
Created on 3/9/22
@author:   Kobe Dawes, Leo Boyer
Pledge:    I pledge my honor that I have abided by the 
        Stevens Honor System. Kobe Dawes Leo Boyer

CS115 - Hw 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
# 31
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.


def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    if (n%2 == 1) is True:
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


def bitCorrect(n):
    '''takes in a number along with the desired bit size and 
    converts the number to binary with the prviously inputted bit amount'''
    bit = COMPRESSED_BLOCK_SIZE
    biNum = numToBinary(n) 

    if len(biNum) == bit:
        return biNum

    else:
        diff = bit - len(biNum)
        return '0'*diff + biNum


def sumTo(string, target, limit):
    '''counts the amount of characters present in a string \
        that is not the target until the limit expires'''

    if string == '':
        return 0
    if string[0] == target:
        return 0
    if limit == 0:
        return 0
    else:
        return 1 + sumTo(string[1:], target, limit - 1) 

count = 0
def compress(n):
    """takes in a 64 bit string and outputs the binary run-length encoding
    of it by the indicated bit and run length"""
    global count
    
    if n == '':
        count = 0
        return ''

    if count % 2 == 0:
        count += 1
        numZeros = sumTo(n, '1', MAX_RUN_LENGTH)
        return bitCorrect(numZeros) + compress(n[numZeros :])
    else:
        count += 1
        numOnes = sumTo(n, '0', MAX_RUN_LENGTH)
        return bitCorrect(numOnes) + compress(n[numOnes :])
        
def uncompress(n):
    """takes in an runlength string and decodes the 
    run length compression """
    global count

    if n == '':
        count = 0
        return ''
    if count % 2 == 0:
        count += 1
        zeros = binaryToNum(n[:COMPRESSED_BLOCK_SIZE]) 
        return '0'*zeros + uncompress(n[COMPRESSED_BLOCK_SIZE:])
    else:
        count += 1
        ones = binaryToNum(n[:COMPRESSED_BLOCK_SIZE]) 
        return '1'*ones + uncompress(n[COMPRESSED_BLOCK_SIZE:])

def compression(s):
    """takes a 64 bit string as the input and gives the
     ratio of the compressed bits to the original size"""
    return len(compress(s))/len(s)

"""we used the penguin test image and with that we 
recieved a compression ration of 1.484375

the professor could not have made such a program because there will 
always be a string like 101010 where the compression will be determined by the CBS, and run-length.
As we set the CBS to reach an optimal run length it is impossible to make such a program, considering 
that such a sequence can be present at any point within a 64 bit string it is definitely impossible for 
this to 'always' be true.
"""

