class Solution:
    def permuteUnique(self, nums):
        ans = []
        path = []
        n = len(nums)
        on_path = [False] * n
        def dfs(i):
            if i == n:
                ans.append(path.copy())
                return
            for j in range(n):
                if on_path[j] or (j > 0 and nums[j] == nums[j-1] and not on_path[j-1]):
                    continue
                path.append(nums[j])
                on_path[j] = True
                dfs(i+1)
                path.pop()
                on_path[j] = False
        dfs(0)
        return ans
solve = Solution()
print(solve.permuteUnique([3,3,0,3]))