#Find the longest increasing subsequence in a list.

def longest_increasing_subsequence(lst):
    if not lst:
        return []
    dp = [1] * len(lst)
    for i in range(len(lst)):
        for j in range(i):
            if lst[i] > lst[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
