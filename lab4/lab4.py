############################################################
# Name:Kobe Dawes
# Pledge:I pledge my honor that I have abided by the Stevens honor system. Kobe Dawes
# CS115 Lab 4
############################################################
def knapsack(limit, itemList): 
    """this function is to take in a weight limit, and a list of weight-value pairs
    and return the maximum value attainable, along with a list of its inteded pairs"""
    if limit == 0:
        return [0, []]
    if itemList == []:
        return [0, []]
    elif itemList[0][0] > limit:
        return knapsack(limit, itemList[1:])
    else:
        useIt = knapsack(limit-itemList[0][0], itemList[1:])
        loseIt = knapsack(limit, itemList[1:])
        jar = [itemList[0][1]+useIt[0], [itemList[0]]+useIt[1]]
        if jar[0] > loseIt[0]:
            return jar
        else:
            return loseIt
#Thank you professor meeting really helped me understand this one
