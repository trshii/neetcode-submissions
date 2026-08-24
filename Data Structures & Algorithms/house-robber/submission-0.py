class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
    
        hs_len = len(nums)
        
        dp = [[0 for _ in range(hs_len + 1)] for _ in range(2)]
        
        for i in range(1, hs_len + 1):
            dp[0][i] = max(dp[0][i-1], dp[1][i-1])
            dp[1][i] = dp[0][i-1] + nums[i-1]
            
        best_sum = max(dp[0][hs_len], dp[1][hs_len])
        
        return best_sum