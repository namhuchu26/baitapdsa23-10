import math

def sol(arr, n):
    g = 0
    for a, b in arr:
        g = math.gcd(g, math.gcd(a, b))
    return g

n = int(input("Nhập số cặp N: "))
arr = [list(map(int, input(f"Nhập cặp {i+1}: ").split())) for i in range(n)]
print("Ước số chung lớn nhất:", sol(arr, n))
