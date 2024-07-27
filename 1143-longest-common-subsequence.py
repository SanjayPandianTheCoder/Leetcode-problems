class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        m = len(text1)+1
        n = len(text2)+1

        dp = [[None]*(n) for i in range(m)]
        print(dp)

        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    dp[i][j] = 0
                elif text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                
        return (dp[m-1][n-1])
                