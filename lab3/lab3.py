############################################################
# Name:Kobe Dawes
# Pledge:I pledge my honor that I have abided by the Stevens honor system. Kobe Dawes
# CS115 Lab 3
############################################################

def change(amount, coinList):
    """this function is to take in an amount and coin list and the output the least amount of coins needed to reach said result"""
    coinList = list(filter((lambda x: x > 0), coinList))
    if amount == 0 :
        return 0
    if amount < 0:
        return float('inf')

    elif amount > 0  and coinList == []:
        return float('inf')

    elif coinList[0] > amount:
        return change(amount, coinList[1:])

    else:
        useIt = 1 + change(amount - coinList[0], coinList) 
        loseIt = change(amount, coinList[1:])
        return min(useIt, loseIt)
        