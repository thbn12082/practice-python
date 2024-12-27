if __name__ == "__main__":
    n = int(input())
    res = 1
    for i in range(n):
        res *= (i + 1)
        res %= (1e9+ 7)
    print(int(res))