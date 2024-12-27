def thuan_ngich(n):
    x = n
    y = 0
    while n != 0:
        y = y*10 + n%10
        n //= 10
    if x == y:
        return True
    else:
        return False

if __name__ == "__main__":
    if thuan_ngich(int(input())):
        print("YES")
    else:
        print("NO")