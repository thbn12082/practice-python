def thap_phan_nhi_phan(n):
    s = ""
    while n // 2 != 0:
        s += str(n%2)
        n //= 2
    if n != 0 : s += "1"
    return s[::-1]

if __name__ == "__main__":
    print(thap_phan_nhi_phan(int(input())))