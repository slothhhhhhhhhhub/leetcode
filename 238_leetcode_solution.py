"""
238 Product of Array Except Self
given an int array, returning an int array
each value in the returning array is the product of all the other elements in the array but not itself

PLAN:
another idea, make a product inner function 
then for that i make it a 1 and find the product of the array with the product function

okay-------------------that didnt work
from the hints i need to use prefix and suffix
so what if i just, for every index, find teh suffic product and prefix product and join them?

"""


class Solution(object):
    def productExceptSelf(self, nums):

        """def product(nums):
            prod = 1 
            for i in range (len(nums)):
                prod = nums[i] * prod

            return prod

        result = []
        for i in range(len(nums)):
            temp = nums[i]
            nums[i] = 1
            result.append(product(nums))
            nums[i] = temp

        return result"""

        n = len(nums)
        result = [1] * n #a list with length n, that's filled with 1s

        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result
        
        