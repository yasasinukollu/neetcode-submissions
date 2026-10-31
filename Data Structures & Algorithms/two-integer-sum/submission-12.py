class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums1 = []
        for i in range(len(nums)):
            nums1.append([nums[i],i])

        nums1 = sorted(nums1)
     
        i = 0
        j = len(nums1)-1

        while i<j:
            if nums1[i][0]+nums1[j][0]==target:
                return [min(nums1[i][1],nums1[j][1]), max(nums1[i][1],nums1[j][1])]
            if nums1[i][0]+nums1[j][0]<target:
                i = i+1
            else:
                j = j-1
        return []