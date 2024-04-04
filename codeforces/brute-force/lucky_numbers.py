# codeforces Lucky Numbers problem
# https://codeforces.com/problemset/problem/1808/A


def lucky(x):
    max_digit = 0
    min_digit = 9
    while x > 0:
        digit = x % 10
        max_digit = max(max_digit, digit)
        min_digit = min(min_digit, digit)
        x //= 10
    return max_digit - min_digit


## Iterative solution
def find_luckiest(l, r):
  luckiest = l
  luck = lucky(l)

  if luck == 9:
    return luckiest
  
  for i in range(l + 1, r + 1):
    current_luck = lucky(i)
    if current_luck == 9:
      luckiest = i
      break

    if current_luck >= luck:
      luckiest = i
      luck = current_luck

  return luckiest


## Recursive solution
def find_luckiest_recursive(l, r, luckiest, luck):
    if l >= r:
        return luckiest
    
    current_luck = lucky(l)
    if current_luck == 9:
        return l
    if luck < 0 or current_luck >= luck:
        return find_luckiest_recursive(l + 1, r, l, current_luck)
    else:
        return find_luckiest_recursive(l + 1, r, luckiest, luck)


test_cases = int(input())
for _ in range(test_cases):
  description = input()
  l, r = map(int, description.split())
  # x = find_luckiest(l, r)
  x = find_luckiest_recursive(l, r, l, -1)
  print(x)