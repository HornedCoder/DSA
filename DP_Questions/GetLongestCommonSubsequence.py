'''
S1 and S2 are given strings, create a function to print all possible longest subsequence which is common to both strings.

Subsequence: a sequence that can be driven from another sequence by deleting some elements without changing the order of them

Example

Input:
 
S1 = "ABCBDAB"
S2 = "BDCABA"
 
Ouput:
 
"BCAB"
"BCBA"
"BDAB"

*****This code is updated version of the previous similar question,here we print all common subsequences.

'''

def findLCS(S1, S2):
    n, m = len(S1), len(S2)
    # Step 1: Build the DP table
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Fill DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if S1[i - 1] == S2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Step 2: Backtrack to find all longest common subsequences
    def backtrack(i, j):
        # If we've reached the start of either string, return a list with an empty string
        if i == 0 or j == 0:
            return {""}
        
        if S1[i - 1] == S2[j - 1]:
            # Characters match, so include this character in the LCS
            lcs_set = backtrack(i - 1, j - 1)
            return {s + S1[i - 1] for s in lcs_set}
        
        # If characters don't match, explore both possible directions
        lcs_set = set()
        if dp[i - 1][j] == dp[i][j]:  # Move up
            lcs_set.update(backtrack(i - 1, j))
        if dp[i][j - 1] == dp[i][j]:  # Move left
            lcs_set.update(backtrack(i, j - 1))
        
        return lcs_set

    # Step 3: Generate and print all LCS of maximum length
    all_lcs = backtrack(n, m)
    for lcs in all_lcs:
        print(lcs)

# Test the function
S1 = "ABCBDAB"
S2 = "BDCABA"
findLCS(S1, S2)

