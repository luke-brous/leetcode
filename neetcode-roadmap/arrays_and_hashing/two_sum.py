# Approach: Using a hash map to store previously seen numbers and their indices.
# For each number, calculate its complement (target - current number).
# Check if the complement exists in the hash map.
# If it does, return the indices of the current number and its complement.
# Time Complexity: O(n) | Space Complexity: O(n)

class Solution(object):
    def twoSum(self, nums, target):

        previous = {}
        cnt = 0
        for i in nums:
            complement = target - i
            if complement not in previous:
                previous[i] = cnt
            elif complement in previous:
                return previous[complement], cnt
            cnt += 1
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        