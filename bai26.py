sinhVien = {
    "hoVaTen" : "Nguyen The Binh",
    "maSinhVien" : "B22DCCN083"
}
print(sinhVien["hoVaTen"])
print(sinhVien)
print(sinhVien.get("maSinhVien"))

#Thay đổi giá trị trong dictionary
sinhVien["maSinhVien"] = "b22dccn083"
print(sinhVien)
sinhVien.update({"hoVaTen" : "Le Minh Ngoc"})
print(sinhVien)
sinhVien.update({"hoVaTen" : "nguyen the binh", "maSinhVien" : "1"})
print(sinhVien)
sinhVien.update({"noiSinh" : "HaNoi"})
print(sinhVien)
sinhVien.pop("maSinhVien")
print(sinhVien)