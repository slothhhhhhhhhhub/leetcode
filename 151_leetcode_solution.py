"""
151 Reverse Words in a String

given a sentence, reverse the words 
removes extra whitespace, 

PLAN: strip them of leading and trailing whitespace 
split by spaces into a list
use two pointers to switch the words order
start one piointer at the start and another at the end, 
while i < j switch them out with a temp var
return the string once done

"""

class Solution(object):
    def reverseWords(self, s):
        s = s.strip()
        sList = s.split()

        i = 0
        j = len(sList) - 1
        while i < j:
            temp = sList[i]
            sList[i] = sList[j]
            sList[j] = temp
            i += 1
            j -= 1

        return " ".join(sList)