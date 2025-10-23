n = int(input("N: "))
m = int(input("M: "))
ds = [tuple(map(int, input().split())) for _ in range(m)]
def demgiao(n, ds):
    l = [[0]*n for _ in range(n)]
    for rt, ct, rd, cd, mau in ds:
        for i in range(rt, rd+1):
            for j in range(ct, cd+1):
                if l[i][j] == 0:
                    l[i][j] = mau
                elif l[i][j] != mau and l[i][j] != 3:
                    l[i][j] = 3
    dem = 0
    for i in range(n):
        for j in range(n):
            if l[i][j] == 3:
                dem += 1
    return dem

print("KQ:", demgiao(n, ds))
