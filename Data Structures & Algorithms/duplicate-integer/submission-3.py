class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_1 = set()
        for i in range(len(nums)):
            if nums[i] in set_1:
                return True
            set_1.add(nums[i])

        return False