class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def permutations(prefix, nums):
            if len(nums) == 1:
                prefix.append(nums[0])
                res.append(prefix)
                return
            for num in nums:
                newPrefix = prefix.copy()
                newPrefix.append(num)
                newNums = nums.copy()
                newNums.remove(num)
                permutations(newPrefix, newNums)
        
        permutations([], nums)
        return res