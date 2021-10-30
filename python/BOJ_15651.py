n, m = map(int, input().split()) # 3, 1 // 4, 2 // 3, 3
out = []

def solve(depth, n, m):
    if depth == m:
        print(' '.join(map(str, out)))
        return
    for i in range(n):
        out.append(i+1)
        solve(depth+1, n, m)
        out.pop()

solve(0, n, m)
