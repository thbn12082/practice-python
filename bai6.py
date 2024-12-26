def ucln(a,b):
    if b == 0:
        return a
    else:
        return ucln(b, a%b)

def bcnn(a,b):
    x = ucln(a,b)
    return int((a*b)/x)

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(ucln(a,b), bcnn(a,b) , end = " ")