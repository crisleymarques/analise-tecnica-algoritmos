# codeforces Tenzing and Balls problem
# https://codeforces.com/problemset/problem/1842/C


def remove_balls(n, colors):
  dp = [0] * (n + 1)
  left_most = [2000000] * (n+1)
  
  dp[0] = 0
  for i in range(1, n + 1):
      dp[i] = dp[i - 1] + 1
      dp[i] = min(dp[i], left_most[colors[i - 1]])
      left_most[colors[i - 1]] = min(left_most[colors[i - 1]], dp[i - 1])
  
  return n - dp[n]


test_cases = int(input())
for _ in range(test_cases):
  n = int(input())
  colors = list(map(int, input().split()))
  print(remove_balls(n, colors))
