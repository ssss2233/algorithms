class Solution:
    def permute(self, nums) :
        permutes = []
        path = []
        def dfs(i,rest):
            if not rest:
                permutes.append(path.copy())
                return 
            for p in rest:
                path.append(p)
                dfs(i+1,rest-{p})
                path.pop()
        dfs(0,set(nums))
        return permutes
solve = Solution()

print(solve.permute([1,2,3]))