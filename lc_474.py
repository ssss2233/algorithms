class Solution:
    def findMaxForm(self, strs, m, n) -> int:
        def dfs(i,m,n):
            if m < 0 or n < 0 or i < 0 or (m == 0 and n == 0):
                return 0
            return max(1+dfs(i-1,m-strs[i].count('1'),n-strs[i].count('0')),dfs(i-1,m,n))
        return dfs(len(strs)-1,m,n)

sol = Solution()
# print(sol.findMaxForm(["10","1","0"],1,1)) # 4

print(sol.findMaxForm(["10","0001","111001","1","0"],5,3)) # 4  