# approach: Brute force would be use a two pointer approach O(n^2) probably not optimal
# Efficient approach would be to use a stack and pop 
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        answer = [0] *len(temperatures)
        stack = []

        for i in range( 0,len(temperatures) ):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                p = stack.pop()
                answer[p] = i - p

            stack.append(i) 

        return answer



        