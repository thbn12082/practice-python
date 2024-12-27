def thap_phan_luc_phan(n):
    s = ""
    while n // 16 != 0:
        x = n % 16
        if x > 9:
            x += 55
            x = chr(x)
        s += str(x)
        n //= 16
    if n != 0:
        if n > 9:
            n += 55
            n = chr(n)
        s += str(n)
    return s[::-1]
if __name__ == "__main__":
    print(thap_phan_luc_phan(int(input())))