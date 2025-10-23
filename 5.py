def sol(a):
    h = [sum(r)//5 for r in a]
    c = [sum(a[j][i] for j in range(5))//5 for i in range(5)]
    return max(h+c) + min(h+c)

a = []
for i in range(5):
    hang = list(map(int, input(f"Hàng {i+1}: ").split()))
    a.append(hang)

print(sol(a))
