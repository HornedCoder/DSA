'''
Length of Longest Palindromic Subsequence
Given a sequence, find the length of the longest palindromic subsequence in it using dynamic programming.

Palindrome is a string that reads the same backward as well as forward.

Example:

lps("ABABCBA") # 5
'''

def lps(S,start,end):
    # TODO
    if start > end:
        return 0
    if S[start] == S[end] and start==end:
        return 1
    if S[start] == S[end]:
        return 2+lps(S,start+1,end-1)
    else:
        return max(lps(S,start+1,end),lps(S,start,end-1))
    


print(lps("ABABCBA",0,6))