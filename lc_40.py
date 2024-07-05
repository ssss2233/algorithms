class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        path = []
        n = len(candidates)
        def dfs(i,rest):
            if rest < 0 or sum(candidates[i:n]) < rest:
                return 
            if rest == 0:
                ans.append(path.copy())
            for j in range(i,n):
                if j > i and candidates[j-1] == candidates[j]:
                    continue
                path.append(candidates[j])
                dfs(j+1,rest-candidates[j])
                path.pop()
        dfs(0,target)
        return ans

# print(solve.combinationSum2([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],30))  # [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
a = [1,2,3,4,5]
print(sum([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))  # 7

