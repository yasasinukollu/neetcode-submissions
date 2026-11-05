class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        result = defaultdict(int)
        for i in nums:
            result[i]+=1
        
        result = sorted(result, key=result.get)
        print(result)
        
        return result[-k:]