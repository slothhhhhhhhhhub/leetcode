"""
643 Maximum Average Subarray I
we are looking for a subarray with length k
this subarray has to have the maximum average value. 

PLAN: the maximum average = max sum/ k
so we need to find the max sum first! 
fun fact there is a sum function which you can use with teh slice notation

for a sliding window i need a window to start sliding, so start by making an inital window. 
to move it, add an element and remove one from the ends. add from the direction you're going and remove from the direction you're leaving. 
"""


class Solution(object):
    def findMaxAverage(self, nums, k):
        windowSum = sum(nums[:k:1])
        maxSum = windowSum

        for i in range(k, len(nums)):
            windowSum += nums[i]
            windowSum -= nums[i - k]

            maxSum = max(maxSum, windowSum)

        maxAverage = float(maxSum) / k
        return maxAverage
        