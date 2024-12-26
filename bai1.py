import math
def demUoc(n):
    cnt = 0
    for i in range(1, n + 1, 1):
        if n % i == 0:
            cnt += 1
        else:
            continue
    return cnt

def tongUoc(n):
    sum = 0
    for i in range(1,n + 1, 1):
        if n % i == 0:
            sum += i
        else:
            continue
    return sum
if __name__ == "__main__":
    n = int(input())
    print(demUoc(n),tongUoc(n), end = " ")


