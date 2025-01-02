
monHoc = {"Toan", "Toan", "Ly","Hoa"}
print(monHoc)
numbers = {1,2,3,22,23,21,4,5,5,5,5,5,6,7,7,4,3,2,1,11}
print(numbers)
sorted(numbers)
print(numbers)
for x in numbers:
    print(x, end = "*")
print()
numbers.add(100)
print(numbers)
print(sorted(numbers))
print(numbers)
updateNumber = {9999,8888,444444,555555,66666}
numbers.update(updateNumber)
print(numbers)
print(sorted(numbers))
numbers.remove(1)
print(numbers)
try:
    numbers.remove(0)
except:
    print("Loi")
numbers = sorted(numbers)
print(numbers)
numbers.pop()
print(numbers)
numbers.pop()
print(numbers)
numbers.pop()
print(numbers)
numbers.pop()
print(numbers)
