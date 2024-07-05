class Solution:
    def partition(self, s):
        ans = []
        path = []
        n = len(s)
        def dfs(i,start):
            if i == n:
                ans.append(path.copy())
                return 
            if(i<n-1):
                dfs(i+1,start)
            
            t = s[start:i+1]
            if t == t[::-1]:
                path.append(t)
                dfs(i+1,i+1)
                path.pop()
        dfs(0,0)
        return ans
solve = Solution()
print(solve.partition('aab'))  # [['a', 'a', 'b'], ['aa', 'b']]