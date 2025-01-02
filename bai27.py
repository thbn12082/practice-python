kiemTraSoChan = lambda a: (a % 2 == 0)
print(kiemTraSoChan(5))

kiemTraTongChan = lambda a,b : ((a+b)%2 == 0)
print(kiemTraTongChan(10,20))

tong = lambda a,b : (a+b)
print(tong(10,20))

def mu(n):
    return lambda x : x**n
