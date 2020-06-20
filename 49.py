'''
Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

Do this in O(N) time.
'''

#My Solution
def Solution(list):
    temp = [0]*len(list)
    temp[0] = list[0]
    res = temp[0]
    for i in range(1,len(list)):
        temp[i] = max(temp[i-1]+list[i], list[i])
        if temp[i] > res:
            res = temp[i]
    
    if res >= 0 :
        return res
    else:
        return 0

#Better Solution
def Solution2(list):
    temp = res = -0
    for x in list:
        temp = max(x, temp+x)
        res = max(res,temp)
    return res

print(Solution2([34, -50, 42, 14, -5, 86]))