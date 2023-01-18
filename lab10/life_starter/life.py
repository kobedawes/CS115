#
# life.py - Game of Life lab
#
# Name: Kobe Dawes
# Pledge: I pledge my honor that I have abided by the Stevens Honor System
#

import random, sys, random

def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You should use this in your
       createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    """ returns a 2d array with "height" rows and "width" cols """ 
    A = []
    for row in range(height):
        A += [createOneRow(width)]    # What do you need to add a whole row here?
    return A

def printBoard( A ):
    """ this function prints the 2d list-of-lists
            A without spaces (using sys.stdout.write)
        """
    for row in A:
        for col in row:
            sys.stdout.write( str(col) )
        sys.stdout.write( '\n' )

def diagonalize(width,height):
    """ creates an empty board and then modifies it
        so that it has a diagonal strip of "on" cells.
    """
    A = createBoard( width, height )
    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A

def innerCells(width,height):
    """ creates an empty board and then modifies it
        so that it has a diagonal strip of "on" cells.
    """
    A = createBoard( width, height )
    for row in range(1, height-1):
        for col in range(1, width-1):
            A[row][col] = 1
    return A

def randomCells(width,height):
    """ creates an empty board and then modifies it
        so that it has a diagonal strip of "on" cells.
    """
    A = createBoard( width, height )
    for row in range(1, height-1):
        for col in range(1, width-1):
            A[row][col] = random.choice( [0,1] )
    return A

def copy(A):
    """takes in a 2D array and returns the copy of its data and not ots reference"""
    newA = createBoard(len(A), len(A[0]))
    for row in range(1, len(A) - 1):
        for col in range(1, len(A[0]) - 1):
            if newA[row][col] != A[row][col]:
                newA[row][col] = A[row][col]
    return newA

def innerreverse(A):
    """takes a 2D array as an input and returns the reverse of it.
     Not including the row of 0s at the begininng and end as well as the ones at the edge"""
    newA = copy(A)
    for row in range(1, len(A) - 1):
        for col in range(1, len(A[0]) - 1):
            if newA[row][col] == A[row][col]:
                newA[row][col] = abs(newA[row][col] -1)
    return newA

def cNeighbors( row, col, A ):
    """ returns the amount of the imemediate neighbors for the cell in the col and row
    """
    newA = copy(A)
    count = 0

    if newA[row-1][col-1] == 1:
        count += 1
    if newA[row-1][col] == 1:
        count += 1
    if newA[row-1][col+1] == 1:
        count += 1

    if newA[row][col-1] == 1:
        count += 1
    if newA[row][col+1] == 1:
        count += 1
        
    if newA[row+1][col-1] == 1:
        count += 1
    if newA[row+1][col] == 1:
        count += 1
    if newA[row+1][col+1] == 1:
        count += 1

    return count
    
def next_life_generation( A ):
    """ makes a copy of A and then advanced one
        generation of Conway's game of life within
        the *inner cells* of that copy.
        The outer edge always stays 0.

    All edge cells stay zero (0) (but see the extra challenges, below)
    2. A cell that has fewer than two live neighbors dies (because of loneliness)
    3. A cell that has more than 3 live neighbors dies (because of over-crowding)
    4. A cell that is dead and has exactly 3 live neighbors comes to life
    5. All other cells maintain their state
    """
    newA = copy(A)
    for row in range(1, len(A) - 1):
        for col in range(1, len(A[0]) - 1):
            neighbors = cNeighbors(row, col, A)

            if neighbors < 2:
                newA[row][col] = 0
            elif neighbors > 3:
                newA[row][col] = 0
            elif neighbors == 3:
                newA[row][col] = 1
    return newA