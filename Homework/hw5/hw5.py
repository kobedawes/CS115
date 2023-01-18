'''
Created on 3/2/22
@author:   Kobe Dawes
Pledge:    I pledge my honor that I have abided by the Stevens Honor System. Kobe Dawes

CS115 - Hw 5 
'''




memo = {}
def fast_lucas(n):
    '''Returns the nth Lucas number using the memoization technique
    shown in class and lab. The Lucas numbers are as follows:
    [2, 1, 3, 4, 7, 11, ...]'''
    if n in memo:
        return memo[n]
    if n == '':
        memo[n] = 'invalid input'
        return  'invalid input'
    if n == 0:
        memo[n] = 2
        return 2
    if n == 1:
        memo[n] = 1
        return 1
    
    else:
        first = fast_lucas(n-2)
        memo[n-2] = fast_lucas(n-2)
        second = fast_lucas(n-1)
        memo[n-2] = fast_lucas(n-1)
        memo[n] = first + second
        return first + second

block = {}
def fast_change(amount, coins):
    '''Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.'''
    coinList = list(filter((lambda x: x > 0), coins))
    coins = tuple(coinList)

    if (amount, coins) in block:
        return block[(amount, coins)]
    if amount == 0 :
        block[(amount, coins)] = 0
        return 0
    if amount < 0:
        block[(amount, coins)] = float('inf')
        return float('inf')

    elif amount > 0  and coinList == []:
        block[(amount, coins)] = float('inf')
        return float('inf')

    elif coinList[0] > amount:
        return fast_change(amount, coinList[1:])

    else:
        useIt =  fast_change(amount - coinList[0], coinList)
        block[(amount - coinList[0], coins)] = fast_change(amount - coinList[0], coinList)

        jar = useIt + 1
        block[(amount, coins)] = useIt + 1
    
        loseIt = fast_change(amount, coinList[1:])
        block[(amount, coins[1:])] = fast_change(amount, coinList[1:])
        return min(jar, loseIt) # min compares the first element of the list and returns the list

        #if jar[0] < loseIt[0]:
        #    return jar
        #else:
        #    return loseIt

# If you did this correctly, the results should be nearly instantaneous.
print(fast_lucas(3))  # 4
print(fast_lucas(4))
print(fast_lucas(5))  # 11
print(fast_lucas(9))  # 76
print(fast_lucas(24))  # 103682
print(fast_lucas(40))  # 228826127
print(fast_lucas(50))  # 28143753123

print(fast_change(131, [1, 5, 10, 20, 50, 100]))
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(673, [1, 5, 10, 20, 50, 100]))
print(fast_change(724, [1, 5, 10, 20, 50, 100]))
print(fast_change(888, [1, 5, 10, 20, 50, 100]))

