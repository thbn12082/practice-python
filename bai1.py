import math
def demUoc(n):
    cnt = 0
    for i in range(1, n + 1, 1):
        if n % i == 0:
            continue
        else:
            cnt += 1
    return cnt

def tongUoc(n):
    sum = 0
    for i in range(1,n + 1, 1):
        if n % i == 0:
            continue
        else:
            sum += i
    return sum
if __name__ == "__main__":
    n = int(input())
    print(demUoc(n),tongUoc(n), end = " ")


