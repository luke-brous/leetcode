# Approach:
# 1. Convert the input list 'nums' into a set to allow O(1) lookups.
# 2. Loop through each number in the set:
#    - If the number is the start of a sequence (num - 1 not in set),
#      count consecutive numbers starting from it.
#    - Keep track of the current streak length and update the longest streak.
# 3. Return the length of the longest consecutive sequence.
# Time Complexity: O(n), where n is the number of unique elements in 'nums'.
# Space Complexity: O(n), due to the set storing all unique numbers.

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums)  # Convert list to set for O(1) lookups
        longest_streak = 0

        for num in nums_set:
            # Only start counting if 'num' is the beginning of a sequence
            if num - 1 not in nums_set:
                current_num = num
                current_streak = 1

                # Count consecutive numbers
                while current_num + 1 in nums_set:
                    current_num += 1
                    current_streak += 1

                # Update the longest streak
                longest_streak = max(longest_streak, current_streak)

        return longest_streak
