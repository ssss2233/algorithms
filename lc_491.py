class Solution:
    def findSubsequences(self, nums):
        res = []
        def dfs(nums, tmp):
            if len(tmp) > 1:
                res.append(tmp)
            curPres = set()
            for inx, i in enumerate(nums):
                if i in curPres:
                    continue
                if not tmp or i >= tmp[-1]:
                    curPres.add(i)
                    dfs(nums[inx+1:], tmp+[i])

        dfs(nums, [])
        return res

solve = Solution()
print(solve.findSubsequences([1,2,3,4,5,6,7,8,9,10,1,1,1,1,1]))


