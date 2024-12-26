import math

def chinh_phuong(n):
    can = int(math.sqrt(n))
    if can*can == n:
        return True
    return False

if __name__ == "__main__":
    if chinh_phuong(int(input())):
        print("YES")
    else:
        print("NO")