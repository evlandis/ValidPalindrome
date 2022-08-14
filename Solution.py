class Solution(object):
    def isPalindrome(self, s):
        newStr = ""
        
        for cha in s:
            #only characters that are letters/numbers
            if cha.isalnum():
                newStr += cha.lower()
        #checking if the regular is the same as the string reversed
        return newStr == newStr[::-1]
