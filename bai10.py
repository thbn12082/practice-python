lst = []
def check_fibo(n):
    lst.append(0)
    lst.append(1)
    if n == 0 or n == 1:
        return True
    else:
        for i in range(2, 92, 1):
            x = lst[i-1] + lst[i-2]
            if n == x:
                return True
            lst.append(x)
    return False
if __name__ == "__main__":
    if check_fibo(int(input())):
        print("YES")
    else:
        print("NO")