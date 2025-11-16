# approach: count consecutive '1's and use the formula n * (n + 1) / 2 to calculate the number of substrings
# time complexity: O(n)
# space complexity: O(1)

class Solution(object):
    def numSub(self, s):
        MOD = 10**9 + 7
        
        ans = 0
        cnt = 0

        for num in range(len(s)):
            if s[num] == "1":
                cnt += 1
            else:
                ans = (ans + cnt * (cnt + 1) // 2) % MOD
                cnt = 0

        ans = (ans + cnt * (cnt + 1) // 2) % MOD

        return ans
