import math


def dem_tong_nguyen_to(n):
    cnt = 0
    sum = 0
    for i in range(1, int(math.sqrt(n)) + 1, 1):
        if n % i == 0:
            if i != n /i:
                cnt += 2
                sum += i + int(n/i)
            else:
                cnt += 1
                sum += int(n/i)
        else:
            continue
    print(cnt, sum, end = " ")

if __name__ == "__main__":
    dem_tong_nguyen_to(int(input()))
