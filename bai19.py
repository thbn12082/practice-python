def luy_thua_nhi_phan(a, b):
    if b == 0:
        return 1
    elif b % 2 == 0:
        return ((luy_thua_nhi_phan(a, b//2) % (1e9+7)) * (luy_thua_nhi_phan(a, b//2) % (1e9+7)))% (1e9+7)
    else:
        return ((luy_thua_nhi_phan(a, b // 2) % (1e9 + 7)) * (luy_thua_nhi_phan(a, b // 2) % (1e9 + 7)) * a)% (1e9+7)
if __name__ == "__main__":
    a, b = map(int, input().split())
    print(int(luy_thua_nhi_phan(a, b)))