############################################################
# Name:Kobe Dawes
# Pledge:I pledge my honor that I have abided by the Stevens honor system. Kobe Dawes
# CS115 Hw 2
############################################################

dictionary = ["a", "am", "at", "apple", "bat", "bar", "babble", "can", "foo",
"spam", "spammy", "zzyzva"]

scrabbleScores = [ ["a", 1], ["b", 3], ["c", 3], ["d", 2], ["e", 1], ["f", 4], ["g", 2], ["h", 4], ["i", 1], ["j", 8], ["k", 5], ["l", 1], ["m", 3], ["n", 1], ["o", 1], ["p", 3], ["q", 10],
 ["r", 1], ["s", 1], ["t", 1], ["u", 1], ["v", 4], ["w", 4], ["x", 8], ["y", 4], ["z", 10] ]
#from functools import reduce
#from collections import counter

def explode(s):
    """takes in a string and puts it into a list with all the characters separated by a space"""
    if s == '':
       return []
    else:
       return [s[0]] + explode(s[1:])


def isSubSet(v2, v1):
    """alternate way to define a subset"""
    v1 = sorted(v1)
    v2 = sorted(v2)
    it = iter(v1)

    return all(c in it for c in v2)


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


def filterD(rack, dictionary):
    """based upon the rack and dictionary variables, this function will return all possible words and their values"""
    if dictionary == [] or rack == '' or rack == []:
        return []
    #if set(explode(dictionary[0])).issubset(set((rack))):
    #if all( i in list(explode(dictionary[0])) for i in rack):
    if isSubSet(explode(dictionary[0]), rack) == True:
        return [[dictionary[0], wordScore(dictionary[0], scrabbleScores)]] + filterD(rack, dictionary[1:])
    else:
        return filterD(rack, dictionary[1:])


def scoreList(rack):
    """does the same thing as filterD but only based upon the rack"""
    return filterD(rack, dictionary)

def bestWord(rack):
    """compares the max values in the liost provided by filterD,
     this function should return the word value pair that has the highest amount"""
    list = filterD(rack, dictionary)

    if scoreList(rack) == [] or rack == '':
        return ['',0]
    else:
        return max(list, key=lambda x:x[1])
