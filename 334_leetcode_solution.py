"""
334 Increasing Triplet Subsequence

we are given a list of numbers , 
and we return true if there are three numbers in ascedninf order

AS: nums must be at have a length of at least 3
we need to have three numbers, 
first is the smallest
second is larger than first
third is the greatest

init first as the smallest(even if it isnt)
init second as some big number

first will track the smallest number
go through the list 
if this value is smaller or equal to the first
    first becomes that number
if it isnt less than first and its smaller than or equal to second
    second becomes that number
if its not less than first, or less than second then it's larger so it is a triplet subseq

"""

class Solution(object):
    def increasingTriplet(self, nums):
        if len(nums) < 3:
            return False

        first = nums[0] 
        second = (2 ** 31)

        for i in range(len(nums)):
            if nums[i] <= first:
                first = nums[i]       
            elif nums[i] <= second:
                second = nums[i]    
            else:
                return True

        return False
        