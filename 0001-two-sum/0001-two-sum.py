class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for x in range(len(nums)):
                if x != i:
                    if nums[x]+nums[i]==target:
                        return [i,x]
            