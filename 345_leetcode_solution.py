"""
345 Reverse Vowels of a String
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"

 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
"""
class Solution(object):
    def reverseVowels(self, s):
        i = 0
        j = len(s) - 1
        sList = list(s)

        while i < j:
            if sList[i] not in "aeiouAEIOU":
                i += 1
            elif sList[j] not in "aeiouAEIOU":
                j -= 1
            else:
                temp = sList[i]
                sList[i] = sList[j]
                sList[j] = temp
                i += 1
                j -= 1
               
        return "".join(sList)