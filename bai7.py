import math

if __name__ == "__main__":
    n, k = map(int, input().split())
    print(math.comb(n, k))