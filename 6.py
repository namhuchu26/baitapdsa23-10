n = int(input("Nhập N: "))
a = list(map(int, input("Nhập phiếu: ").split()))
def sol(n, a):
    d = {}
    for x in a:
        d[x] = d.get(x, 0) + 1
    mx = max(d.values())
    return max(k for k, v in d.items() if v == mx)

print("Sốt ngon nhất:", sol(n, a))
