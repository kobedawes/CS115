############################################################
# Name:Kobe Dawes
# Pledge:I pledge my honor that I have abided by the Stevens honor system. Kobe Dawes
# CS115 Hw3
#apologies for the late submittal I tried asking for an extension but don't know if it was granted
############################################################


def giveChange(amount, coinList):
    """this function is to take in an amount and coin list and the output the least amount of coins needed to reach said result"""
    coinList = list(filter((lambda x: x > 0), coinList))
    if amount == 0 :
        return [0, []]
    if amount < 0:
        return [float('inf'), []]

    elif amount > 0  and coinList == []:
        return [float('inf'), []]

    elif coinList[0] > amount:
        return giveChange(amount, coinList[1:])

    else:
        useIt =  giveChange(amount - coinList[0], coinList) 
        jar = [useIt[0]+1, [coinList[0]] + useIt[1]]
        loseIt = giveChange(amount, coinList[1:])
        return min(jar, loseIt) # min compares the first element of the list and returns the list
        #if jar[0] < loseIt[0]:
        #    return jar
        #else:
        #    return loseIt

print(giveChange(30, [1, 10, 5, 20]))

scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def letterScore(letter, scorelist):
    """ takes in a letter and compares it to a list of letters associated with a value,
     if the letters are the same the function will print the value"""
    if letter == '' or scorelist == []:
        return 0
    if letter == scorelist[0][0]:
        return scorelist[0][1]
    else:
        return letterScore(letter, scorelist[1:])


def wordScore(s, scorelist):
    """Takes a word and counts the value of its individual letters"""

    if s == '' or s == [] or scorelist == []:
        return 0
    
    else:
        return letterScore(s[0], scorelist) + wordScore(s[1:], scorelist)

def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.
    Assume dct is a list of words, and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    '''
    if dct == []  or scores == []:
        return []
    else:
        value = wordScore(dct[0],scores)
        return [[dct[0], value]] + wordsWithScore(dct[1:], scores)
   
        



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
' (Notice that you cannot assume anything about the length of the list.)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n], assuming L is a list and n is at least 0.'''
    """L[0:0] returns '' nothing if used with a list"""
    basket = []
    if L == []:
        return []
    if n < 0: 
        return []
    if n == 0:
        return []
    else:
        return [L[0]]+ take(n-1, L[1:])



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:], assuming L is a list and n is at least 0.'''
    if L == []:
        return []
    if n < 0: 
        return []
    if n == 0:
        return L
    if len(L) < n:
        return []
    else:
        return drop(n-1, L[1:])
     
