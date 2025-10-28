# approach: create a sorted list of strings, create a hasmap that uses the sorted
# str as keys that makes a list of the anagrams
# return the values as a list

# Time Complexity: O(n * k log k), Space Complexity: O(n * k)


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sorted_list = []

        hash = {}

        for str in strs:
            sorted_str = ''.join(sorted(str))
            
            sorted_list.append(sorted_str)
            if sorted_str not in hash:
                hash[sorted_str] = [str]
            else:
                hash[sorted_str].append(str)

        return list(hash.values())
            

            

            
                 
            
            


