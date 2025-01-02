#có 2 cách khởi tạo list
emptyList = []
emptyList2 = list()
emptyList.append(1)
emptyList.append("binh")
emptyList.append("ngoc")
print(emptyList2)
print(emptyList)


# tạo ra list có dữ liệu:
colors = ["red", "yellow", "green"]
print(colors)

studentList = ["An", "Binh", "Ngoc"]
print(studentList)
print(studentList[1])
print(studentList[2])
print(studentList[1:3])
print(studentList[1:])
studentList.insert(1,"Ngoc")
print(studentList)
print(len(studentList))
print(studentList.count("Binh"))
studentList.remove("An")
#xóa 1 phần tử An đầu tiên thôi không xóa tất cả An
print(studentList)
if "Ngoc" in studentList:
    print("YES")
else:
    print("NO")
#xóa phần tử bằng vị trí của nó
print(studentList.pop(0))
print(studentList)
print(*studentList)
print(studentList[::-1])
studentList.sort()
print(studentList)

#sắp xếp
numbers = [1,2,3,4,5,21,22,23,6,7,8,56,66]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

#xóa sạch list
numbers.clear()
print(numbers)