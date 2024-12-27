lst = []
def fibo():
    lst.append(0)
    lst.append(1)
    for i in range (2, 92, 1):
        lst.append(lst[i-2] + lst[i-1])

if __name__ == "__main__":
    fibo()
    print(lst)