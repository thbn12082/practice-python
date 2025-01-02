class Person:
    nationality = "Viet Nam"
    def __init__(self, name, job):
        self.name = name
        self.job = job

class SinhVien:
    truong = "PTIT"
    def __init__(self, ten, maSinhVien, queQuan):
        self.ten = ten
        self.maSinhVien = maSinhVien
        self.queQuan = queQuan
    def greet(self):
        print("xin chao")

if __name__ == '__main__':
    # p1 = Person("Nguyen The Binh", "IT")
    # p2 = Person("Le Minh Ngoc", "DTVT")
    #
    # print(p1.nationality, p1.name, p1.job, end=" ")
    # print()
    # print(p2.nationality, p2.name, p2.job, end= " ")
    # print()
    s1 = SinhVien("Nguyen The Binh", "B22DCCN083", "HaNoi")
    s2 = SinhVien("Le Minh Ngoc", "B22DCCN863", "Ha Noi")
    print(s1.truong, s1.ten,s1.maSinhVien, s1.queQuan)
    print(s2.truong, s2.ten,s2.maSinhVien, s2.queQuan)
    s1.greet()
    s2.greet()