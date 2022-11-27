class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        # ans=[]
        # for i in nums:
        #     ans.append(nums[nums[i]])
        ans = [nums[nums[i]] for i in range(len(nums))]
        return ans