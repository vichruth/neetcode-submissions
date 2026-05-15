import collections
class Solution: 
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Map character count tuple to list of anagrams
        ans = collections.defaultdict(list)

        for s in strs:
            # Create a frequency histogram for the 26 lowercase English letters
            count = [0] * 26
            
            for char in s:
                # ord() gets the ASCII value. ord('a') - ord('a') = 0, ord('b') - ord('a') = 1
                count[ord(char) - ord('a')] += 1
                
            # Tuples are immutable and therefore hashable in Python
            # We use the frequency histogram as the canonical key
            ans[tuple(count)].append(s)

        # Return the grouped arrays
        return list(ans.values())