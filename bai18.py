def to_hop_chap_2(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return to_hop_chap_2(n-1, k - 1) + to_hop_chap_2(n - 1, k)

if __name__ == "__main__":
    n, k = map(int, input().split())
    print(to_hop_chap_2(n, k))