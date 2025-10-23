n = int(input("N: "))
m = int(input("M: "))
ds = [tuple(map(int, input().split())) for _ in range(m)]
def tinh(n, ds):
    v = [[0]*n for _ in range(n)]
    for y, x, w in ds:
        for c in range(max(0, x-w), min(n-1, x+w)+1):
            v[y][c] = 1
        for r in range(max(0, y-w), min(n-1, y+w)+1):
            v[r][x] = 1
    k = 0
    for r in range(n):
        for c in range(n):
            if v[r][c] == 0:
                k += 1
    return k

print("KQ:", tinh(n, ds))
