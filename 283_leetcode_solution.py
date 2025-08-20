"""
283 Move Zeroes

we get a list of numbers and we have to move all the numbers to the end of it, the right side of it

Plan: 
second plan. have two pointers. one to keep track of the non-zero elements and where they are/can be
the second pointer to iterate through the list
check to see if a value isnt 0 then put it wherever the pointer says it can be
iterate the non-zero pointer then 

"""

class Solution(object):
    def moveZeroes(self, nums):
        nonZero = 0

        for i in range (len(nums)):
            if not nums[i] == 0:
                temp = nums[nonZero]
                nums[nonZero] = nums[i]
                nums[i] = temp
                nonZero += 1

        return nums
        