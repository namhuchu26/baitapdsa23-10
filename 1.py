n = int(input("Nhập số phần tử N: "))
m = int(input("Nhập số M: "))
arr = list(map(int, input("Nhập mảng: ").split()))


def tinh_tong(arr, m):
    arr = sorted(arr)
    tong = 0
    for i in range(m, len(arr), m):
        tong += arr[i]
    return tong


kq = tinh_tong(arr, m)
print("Tổng các phần tử có chỉ số bội số của", m, "là:", kq)
