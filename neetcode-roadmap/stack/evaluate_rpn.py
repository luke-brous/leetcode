class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
    
        stack = []

        for val in tokens:
            # check for operand, keep going
            # check for operators pop last 2 values and push ans
            if val not in {"+", "-", "*", "/"}:
                stack.append(int(val))
            else:
                val2 = stack.pop()
                val1 = stack.pop()

                if val == "-": 
                    stack.append(val1 - val2)
                elif val == "+":
                    stack.append(val1 + val2)
                elif val == "/": 
                    stack.append(int(float(val1) / val2))
                elif val == "*": 
                    stack.append(val1 * val2)

            


        return stack.pop()

