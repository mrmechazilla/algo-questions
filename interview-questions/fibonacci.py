# Recursive Approach

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

# Dynamic programming Approach
def fib(n):
    memo = {0: 0, 1: 1}  # base cases

    def dp(k):
        if k in memo:
            return memo[k]
        memo[k] = dp(k - 1) + dp(k - 2)
        return memo[k]

    return dp(n)