class Solution:
    def combinationSum(self, candidates, target):
        ans = []
        path = []
        n = len(candidates)
        def dfs(i,rest):
            if(rest < 0):
                return 
            if(sum(path) == target):
                ans.append(path.copy())
                return 
            for j in range(i,n):
                path.append(candidates[j])
                dfs(j,rest-candidates[j])
                path.pop()
        dfs(0,target)
        return ans
solve = Solution()
print(solve.combinationSum([2,3,6,7],7))  # [[2, 2, 3], [7]]