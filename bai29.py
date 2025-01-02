def ucln(a, b):
    if b == 0:
        return a
    else:
        return ucln(b, a%b)
class PhanSo:
    def __init__(self, tuSo, mauSo):
        self.tuSo = tuSo
        self.mauSo = mauSo
        tmp = ucln(self.tuSo, self.mauSo)
        self.tuSo = self.tuSo // tmp
        self.mauSo = self.mauSo // tmp

    def __str__(self):
        if self.mauSo != 1:
            return f'{self.tuSo}/{self.mauSo}'
        else:
            return f'{self.tuSo}'
if __name__ == "__main__":
    x, y = map(int, input().split())
    a = PhanSo(x, y)
    print(a)