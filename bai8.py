import math

def to_hop_chap(n,k):
    return (math.factorial(n)) // (math.factorial(k)* math.factorial(n - k))

if __name__ == "__main__":
    n, k = map(int, input().split())
    print(to_hop_chap(n,k))