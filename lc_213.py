class Solution:
    def rob(self, nums) -> int:
        def dfs(start,end):
            if start < 0 or end > start:
                return 0
            if end == len(nums) - 1:
                return max(dfs(start,end-1),nums[end] + dfs(start+1,end-2))
            return max(dfs(start,end-1),nums[end] + dfs(start,end-2))
        return dfs(0,len(nums)-1)
    
solve = Solution()
print(solve.rob([1,2,3])) # 4