import math

def so_hoan_hao(n):
    sum = 1
    for i in range(2, int(math.sqrt(n)) + 1, 1):
        if n % i == 0:
           if i != n//i:
               sum += i + n//i
           else:
               sum += i
    if sum == n:
        return True
    else:
        return False

if __name__ == "__main__":
    if so_hoan_hao(int(input())):
        print("YES")
    else:
        print("NO")