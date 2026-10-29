class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i in range(len(nums)):
            hmap[nums[i]] = i

        
        for j in range(len(nums)):
            if target-nums[j] in hmap:
                if j != hmap[target-nums[j]]:
                    return [j, hmap[target-nums[j]]]

        return []