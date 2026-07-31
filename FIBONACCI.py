# Memoization (Top-Down Dynamic Programming)
def fibonacci_memo(n, memo=None):
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


# Tabulation (Bottom-Up Dynamic Programming)
def fibonacci_tab(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# Main Program
if __name__ == "__main__":
    n = int(input("Enter the value of n: "))

    print(f"\nUsing Memoization: Fibonacci({n}) = {fibonacci_memo(n)}")
    print(f"Using Tabulation: Fibonacci({n}) = {fibonacci_tab(n)}")