class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pairs = {
           '{': '}',
           '(': ')',
           '[': ']'
        }       
        stack = []

        for char in s:
            if (char == "(" or char == "{" or char == "["):
                stack.append(char)
            elif len(stack) == 0:
                return False
            
            # Pop the top item off the stack and check if it matches
            elif char != pairs[stack.pop()]:
                return False
        return len(stack) == 0

            