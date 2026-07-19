class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        n = len(nums)
        duplicate = -1
        for i in range(1, n):
            if nums[i] == nums[i-1]:
                duplicate = nums[i]
                break
        
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        missing = expected_sum - (actual_sum - duplicate)
        
        return [duplicate, missing]