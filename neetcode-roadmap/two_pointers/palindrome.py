import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        
        r = len(s) - 1 
        print(s)
        for l in range(len(s)):
            if (s[l] != s[r]):
                return False
            r -= 1
        
        return True
