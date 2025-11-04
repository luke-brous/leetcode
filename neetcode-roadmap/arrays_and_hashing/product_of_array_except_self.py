# approach: create two arrays, one for the prefix products and one for the suffix products
# then multiply the corresponding elements from each array to get the final result
# time complexity: O(n), space complexity: O(n)
# this code is not optimal, optimal solution uses O(1) space



class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = []
        prefix = []
        suffix = []

        prd = 1
        for i in range(len(nums)):
            prefix.append(prd)
            prd *= nums[i]
        
        prd = 1
        for i in range(len(nums) - 1, -1, -1):
            suffix.append(prd)
            prd *= nums[i]

        
        for i in range(len(prefix)):
            answer.append(prefix[i] * suffix[len(suffix) - 1 - i])

        return answer