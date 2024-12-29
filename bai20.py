def tinh_tong(n):
    if n == 1:
        return 1
    else:
        return 1/n + tinh_tong(n - 1)

if __name__ == "__main__":
    print(f"{tinh_tong(int(input())):.3f}")