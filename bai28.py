class Person:
    nationality = "Viet Nam"
    def __init__(self, name, job):
        self.name = name
        self.job = job
    def __del__(self):
        print("Da xoa Person")
    def __str__(self):
        return f'{self.name} {self.job}'

class SinhVien:
    truong = "PTIT"
    def __init__(self, ten, maSinhVien, queQuan):
        self.ten = ten
        self.maSinhVien = maSinhVien
        self.queQuan = queQuan
    def greet(self):
        print("xin chao")
    def info(self):
        print(self.ten, self.maSinhVien, self.queQuan)
    def __del__(self):
        print("Da xoa Sinh Vien")
    def __str__(self):
        return f'{self.ten} {self.maSinhVien} {self.queQuan} {self.truong}'
class ThongTinSinhVien:
    def __init__(self, ten, tuoi, que):
        self.ten = ten
        self._tuoi = tuoi
        self.__que = que
    def outThongTin(self):
        print('ten : {}, tuoi : {}, queQuan :{}'.format(self.ten, self._tuoi, self.__que))
    def getName(self):
        return self.ten
    def __del__(self):
        print("Da xoa thong tin sinh vien ")
    def __str__(self):
        return f'{self.ten} {self._tuoi} {self.__que}'
if __name__ == '__main__':
    p1 = Person("Nguyen The Binh", "IT")
    p2 = Person("Le Minh Ngoc", "DTVT")
    print(p1.nationality, p1.name, p1.job, end=" ")
    print()
    print(p2.nationality, p2.name, p2.job, end= " ")
    print()
    print(p1)
    print(p2)

    del p1
    del p2
    s1 = SinhVien("Nguyen The Binh", "B22DCCN083", "HaNoi")
    s2 = SinhVien("Le Minh Ngoc", "B22DCCN863", "Ha Noi")
    print(s1.truong, s1.ten,s1.maSinhVien, s1.queQuan)
    print(s2.truong, s2.ten,s2.maSinhVien, s2.queQuan)
    print(s1)
    print(s2)
    s1.greet()
    s2.greet()
    s1.info()
    s2.info()
    del s1
    del s2
    s3 = ThongTinSinhVien("Nguyen The Binh", 21, "Ha Noi")
    s3.outThongTin()
    print(s3.getName())
    print(s3)
    del s3