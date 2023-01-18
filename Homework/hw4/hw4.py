############################################################
# Name:Kobe Dawes
# Pledge:I pledge my honor that I have abided by the Stevens honor system. Kobe Dawes
# CS115 hw4
############################################################

memo = {}
memo2 = {}


def middle(n):
    """helper function that takes in a list and
     outputs a list that is the sum of the first two numbers"""
    if n == []:
        return []
    if n == [1]:
        return []

    elif len(n) == 1:
        return []
    
    else:
        return [n[0] + n[1]] + middle(n[1:]) 


def pascal_row(n):
    """takesn an integer as an innput and creates that specific row as a list"""
    if n in memo:
        return memo[n]

    if n < 0:
        return 'invalid input'
    
    elif n == 0:
        memo[n] = [1]
        return [1]
    else:
        term = middle(pascal_row(n-1))
        memo[n] = [1] + term + [1]
        return [1] +term + [1] 


def pascal_triangle(n):
    """prints the list of pascal's triangle in ascedning order"""
    if n in memo2:
        return memo2[n]
    if n == []:
        return []
    if n == 0:
        memo2[n] = [[1]]
        return [[1]]
    
    if n < 0:
        return 'invalid input'
    
    else:
        triangle = pascal_triangle(n-1)
        row = [pascal_row(n)]
        memo2[n] = triangle + row
        return  triangle + row


def test_pascal_row():
    """tests pascal_row"""
    assert pascal_row(0)== [1]
    assert pascal_row(1) == [1,1]
    assert pascal_row(5) == [1,5,10,10,5,1]
    assert pascal_row(15) == [1, 15, 105, 455, 1365, 3003, 5005, 6435, 6435, 5005, 3003, 1365, 455, 105, 15, 1]


def test_pascal_triangle():
    """tests pascal_triangle"""
    assert pascal_triangle(0) == [[1]]
    assert pascal_triangle(1) == [[1],[1,1]]
    assert pascal_triangle(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
    assert pascal_triangle(7) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1], [1, 7, 21, 35, 35, 21, 7, 1]]