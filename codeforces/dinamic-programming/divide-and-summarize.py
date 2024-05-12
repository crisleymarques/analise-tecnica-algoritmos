# codeforces Divide and Summarize problem
# https://codeforces.com/problemset/problem/1461/D

# Utilizando busca binária para encontrar o valor médio entre os valores de a[s] e a[e] e dividir o array em dois

def prettiness(s, e, a, poss, pre_sum):
    poss.add(pre_sum[e + 1] - pre_sum[s])
    
    if a[s] == a[e]:
        return
    
    l, h = s, e + 1
    val = (a[s] + a[e]) // 2
    while l < h:
        mid = (l + h) // 2
        if a[mid] <= val:
            l = mid + 1
        else:
            h = mid
            
    pivot = h - 1
    prettiness(s, pivot, a, poss, pre_sum)
    prettiness(pivot + 1, e, a, poss, pre_sum)


test_cases = int(input())
for _ in range(test_cases):
    n, q = map(int, input().split())
    poss = set()
    
    a = list(map(int, input().split()))
    a.sort()
    
    pre_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        pre_sum[i] = pre_sum[i - 1] + a[i - 1]
    
    prettiness(0, n - 1, a, poss, pre_sum)
    
    for _ in range(q):
        s = int(input())
        print("yes" if s in poss else "no")
