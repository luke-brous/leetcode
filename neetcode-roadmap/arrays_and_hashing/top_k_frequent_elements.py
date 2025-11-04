# approach: loop through nums and create a hashmap of the frequencies of each num
# then return the k most frequent element by iterating through the hashmap
# Time Complexity: O(n*m)


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hash = {}
        ans = []

        for num in nums:
            if num not in hash:
                hash[num] = 1
            else:
                hash[num] += 1
        
        max_frequency = max(hash.values()) # you're stupid and couldn't figure this out
        buckets = [[] for _ in range(max_frequency + 1)] # you're stupid and couldn't figure this out

        
        
        for key, value in hash.items():
            buckets[value].append(key)

        
        for i in range(max_frequency,0,-1):
            for j in buckets[i]:
                ans.append(j)

            if len(ans) == k:
                return ans
        return ans
