# class Solution:
#     def combine(self, n: int, k: int) :
#         ans = []
#         path = []
#         def dfs(i):
#             if len(path) == k:
#                 ans.append(path.copy())
#                 return 
#             for j in range(i,n+1):
#                 path.append(j)
#                 dfs(j+1)
#                 path.pop()
#         dfs(1)
#         return ans
class Solution:
    def combine(self, n: int, k: int) :
        ans = []
        path = []
        def dfs(i):
            if len(path) == k:
                ans.append(path.copy())
                return 
            if i<n-k+len(path)+1:
                dfs(i+1)
            path.append(i)
            dfs(i+1)
            path.pop()
        dfs(1)
        return ans
solve = Solution()
print(solve.combine(4,2))  # [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]