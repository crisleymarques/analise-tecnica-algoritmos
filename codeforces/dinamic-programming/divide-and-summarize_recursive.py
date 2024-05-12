# codeforces Divide and Summarize problem
# https://codeforces.com/problemset/problem/1461/D


def mid(a):
  return (max(a) + min(a)) // 2


def prettiness(a, s, current_sum):
  if current_sum == s:
    return True

  if len(a) == 1 or current_sum < s or a[0] == a[-1]:
    return False

  m = mid(a)
  left = [x for x in a if x <= m]
  right = [x for x in a if x > m]

  left_answer = prettiness(left, s, sum(left))
  right_answer = prettiness(right, s, sum(right))

  if left_answer or right_answer:
    return 'yes'
  return 'no'

  
test_cases = int(input())
for _ in range(test_cases):
  n, q = map(int, input().split())
  a = list(map(int, input().split()))
  a = sorted(a)
  for _ in range(q):
    s = int(input())
    print(prettiness(a, s, sum(a)))
