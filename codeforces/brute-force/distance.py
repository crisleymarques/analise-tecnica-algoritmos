# codeforces Distance problem
# https://codeforces.com/problemset/problem/1612/A


def distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def find_C(x2, y2):
    x1, y1 = 0, 0
    x3, y3 = -1, -1
    found = False

    half_d_A_B = distance(x1, y1, x2, y2) / 2

    for x in range(x2 + 1):
      for y in range(y2 + 1):
        if found: 
          break

        d_A_C = distance(x1, y1, x, y)
        d_B_C = distance(x2, y2, x, y)

        if d_A_C == half_d_A_B and d_B_C == half_d_A_B:
          if x >= 0 and y >= 0:
            x3, y3 = x, y
            found = True

    return x3, y3


test_cases = int(input())
for _ in range(test_cases):
  coordenadas = input()
  x2, y2 = map(int, coordenadas.split())
  x3, y3 = find_C(x2, y2)
  print(x3, y3)