n = int(input("só phần tủ mảng: "))
m = int(input("độ dài dãy con ma: "))
a = list(map(int, input("Mảng: ").split()))
def sol(a, n, m):
    s = [sum(a[i:i+m]) for i in range(n - m + 1)]
    return max(s) - min(s)

print(sol(a, n, m))
