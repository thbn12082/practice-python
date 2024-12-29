u = """
Cuoc doi toi that
tuyet 
voi """
print(u)

for x in u :
    print(x, end = " ")
print()

for i in range(len(u)):
    print(u[i], end = " ")

print()
s = "28tech"
print(s[1:4])
print(s[2:])
print(s[::-1])

t = s[::]
print(t)

a = ['nguyen', 'the', 'binh']
print(' '.join(a))
print(" - ".join(a))


x = "nguyen the binh "
print(x.upper())
print(x.lower())
print(x.capitalize())
print(x.swapcase())
print(x.title())

if "the" in x:
    print("FOUND")

print(x.find("the"))
print(x.find('nguyen'))
print(ord('A'))
print(chr(65))