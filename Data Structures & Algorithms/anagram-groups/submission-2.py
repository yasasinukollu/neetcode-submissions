from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for words in strs:
            c = [0] * 26
            for chrs in words:
                c[ord(chrs)-ord('a')] += 1

            result[tuple(c)].append(words)
        
        return list(result.values())

