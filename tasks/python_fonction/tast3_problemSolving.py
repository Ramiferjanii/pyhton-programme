



#
# Complete the 'renameFile' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING newName
#  2. STRING oldName
#

def renameFile(newName, oldName):
    MOD = 10**9 + 7
    
    # lengths of newName and oldName
    m, n = len(newName), len(oldName)
    
    # dp[i][j] will store the count of ways to form newName[:i] from oldName[:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Base case: There's exactly one way to form an empty string from any substring of oldName
    for j in range(n + 1):
        dp[0][j] = 1
    
    # Fill dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # If the characters match, we can either use the current character or skip it
            if newName[i - 1] == oldName[j - 1]:
                dp[i][j] = (dp[i - 1][j - 1] + dp[i][j - 1]) % MOD
            else:
                # Otherwise, we can only skip the current character in oldName
                dp[i][j] = dp[i][j - 1]
    
    # The answer is the number of ways to form newName from oldName
    return dp[m][n]

