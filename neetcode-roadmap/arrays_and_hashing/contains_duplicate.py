# Intuition: Describe your first thought on how to solve this problem.
# Best approach, use a hasmap for every # and loop through array

# Approach: Describe your approach to solving the problem.
# loop through array, check if its in set: if yes --> true ; if no --> false


# Time Complexity: O() | Space Complexity: O()
# time O(n) because each element is being checked once, space O(n) for storing seen elements in the set

# Code
class Solution(object):
    def containsDuplicate(self, nums):
        hash = {}
        for num in nums:
            if (num in hash) :
                return True
            else :
                hash[num] = True

        return False
            

        
        