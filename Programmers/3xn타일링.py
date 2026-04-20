def solution(n):
    if n % 2 != 0:
        return 0
    if n == 2:
        return 3
    dp = [0] * (n + 1)
    dp[0] = 1 
    dp[2] = 3

    # f(n) = 3f(n-2) + 2f(n-4) + 2f(n-6) + .... + 2f(0) 식을 하나 더 만들고 두 식을 빼서 점화식을 구함
    for i in range(4, n + 1, 2):
        dp[i] = 4 * dp[i-2] - dp[i-4]

    return dp[n] % 1000000007