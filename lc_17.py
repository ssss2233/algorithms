MAPPING = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

class Solution:
    def letterCombinations(self, digits):
        n = len(digits)
        if n == 0:
            return []
        ans = []
        path = [''] * n  # 本题 path 长度固定为 n
        def dfs(i: int) -> None:
            if i == n:
                ans.append(''.join(path))
                return
            for c in MAPPING[int(digits[i])]:
                path[i] = c  # 直接覆盖
                dfs(i + 1)
        dfs(0)
        return ans
solution1 = Solution()
print(solution1.letterCombinations('23'))  # ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]