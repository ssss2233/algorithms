class Solution:
    def subsetsWithDup(self, nums):
        subset = []
        path = []
        n = len(nums)
        def dfs(i):
            subset.append(path.copy())
            if i == n:
                return
            for j in range(i,n):
                if j>i and nums[j] == nums[j-1]:
                    continue
                path.append(nums[j])
                dfs(j+1)
                path.pop()
        dfs(0)
        return subset
solve = Solution()
print(solve.subsetsWithDup([1,2,2]))