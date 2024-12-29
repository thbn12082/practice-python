if __name__ == "__main__":
    cnt = [0]*256
    s = input()
    d = dict({})
    for i in s:
        cnt[ord(i)] += 1
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    for i in range(256):
        if cnt[i] != 0:
            print(chr(i), cnt[i])
    print()
    for i in s:
        if cnt[ord(i)] != 0:
            print(i, cnt[ord(i)])
            cnt[ord(i)] = 0
    print()
    for x, y in d.items():
        print(x, y)
    print()
    for x in sorted(d):
        print(x, d[x])