import math

def phan_tich_thua_so_nguyen_to(n):
    for i in range(2, int(math.sqrt(n)) + 1, 1):
        if n % i == 0:
            while n % i == 0:
                n //= i
                print(i, end = " ")
        else:
            continue
    if n != 1:
        print(n)
if __name__ == "__main__":
    phan_tich_thua_so_nguyen_to(int(input()))