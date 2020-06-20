'''
Given a array of numbers representing the stock prices of a company in chronological order, write a 
function that calculates the maximum profit you could have made from buying and selling that stock once. 
You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars 
and sell it at 10 dollars.
'''

#My Solution

def solution(prices):
    lowest = prices[0]
    res = 0
    if p < lowest:
        lowest = p
    for p in prices:
        res = max(res, p-lowest)
    return res

print(solution([9, 11, 8, 5, 7, 10]))
    