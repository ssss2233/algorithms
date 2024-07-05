class Solution:
    def findLength(self, nums1, nums2) -> int:
        dp = [[0] * (len(nums1)+1) for _ in range(len(nums2)+1)]
        res = 0
        for i in range(len(nums2)-1,-1,-1):
            for j in range(len(nums1)-1,-1,-1):
                dp[i][j] = dp[i+1][j+1] + 1 if nums1[i] == nums2[j] else 0
                res = max(res,dp[i][j])
        return res
solve = Solution()
print(solve.findLength([1,2,3,2,1],[3,2,1,4])) # 3