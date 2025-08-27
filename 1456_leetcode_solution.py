"""
1456 Maximum Number of Vowels in a Substring of a Given Length

all lowercase letters

PLAN: make s a list so i can iterate in peace. 
will have two variables, one for the number of vowles in the window and another to keep the max value. so i can compare the two. 

first start by making teh window var 

"""

class Solution(object):
    def maxVowels(self, s, k):
        sList = list(s)
        
        windowVow = 0
        for i in range(k):
            if sList[i] in "aeiou":
                windowVow += 1

        maxVow = windowVow
        
        for i in range(k, len(sList)):
            """
            move the window
            check and add any vowels
            compare max
            """
            if sList[i] in "aeiou":
                windowVow += 1

            if sList[i - k] in "aeiou":
                windowVow -= 1

            maxVow = max(maxVow, windowVow)

        return maxVow
        
        