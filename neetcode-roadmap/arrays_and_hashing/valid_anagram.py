# use a hashmap to record every letter in each word,
# then check both hasmaps to make sure they're the same
# return true or false
# should be O(n) with hashmaps

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        hash_s = {}
        hash_t = {}

        for i in s:
            if i in hash_s:
                hash_s[i] += 1 
            else:
                hash_s[i] = 1
        print(hash_s)

        for j in t:
            if j in hash_t:
                hash_t[j] += 1 
            else:
                hash_t[j] = 1
        
        if hash_t == hash_s:
            return True
        else:
            return False
         



        