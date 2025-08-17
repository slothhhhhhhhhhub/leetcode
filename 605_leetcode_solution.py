"""
605 Can Place Flowers
the flower bed is a array, each index is a spot to plant a flower

Plan: iterate through the lits, check the adjacent plots, check if its empty then place a flower and keep it pushing?
return if n is finished meaning fi all flowers are placed
"""


class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        length = len(flowerbed)

        i = 0
        while i < length and n >= 0:
            if flowerbed[i] == 0:
                leftEmpty = (i == 0) or (flowerbed[i - 1] == 0)
                rightEmpty = (i == (length - 1)) or (flowerbed[i + 1] == 0)
                if leftEmpty and rightEmpty:
                    flowerbed[i] = 1
                    n -= 1
                    i += 1

            i += 1

        return n <= 0

        