import math
def nt(n):
    if n < 2 :
        return False
    for i in range(2, int(math.sqrt(n)) + 1, 1):
        if n % i == 0:
            return False
    return True
if __name__ == "__main__":
    if nt(int(input())):
        print("YES")
    else:
        print("NO")