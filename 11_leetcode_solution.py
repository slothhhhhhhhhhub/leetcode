"""
11 Container with Most Water
input is height list. with a length n. 
n is also the number of vertical lines that are possible container walls.
 
area is height * width
height is the minumum value between the values in the list
the width is the j - i

so find the product at each time then do the checks to see if it is larger than the result


"""

class Solution(object):
    def maxArea(self, height):
        result = 0

        i = 0
        j = len(height) - 1

        while i < j:
            containerWidth = j - i
            containerHeight = min(height[i], height[j])
            area = containerWidth * containerHeight

            result = max(result, area)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1


        return result


        