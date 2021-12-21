a = [1,2,3,4,5,6]
print("a: ",a)

print("Copy entire list")
print("Creating a copy of var a into b")
print("b = a")
b = a 
print(b)

print("list[ start : stop : step ]")
print("rev_b = b[::-1]: ")
rev_b = b[::-1]
print(rev_b)

print("Step of 2.")
print("a[::2]: ")
print(a[::2])

print("copy with slice")
c = b[:3]
print(c)

d = [1, 2, 4, 6, [7,2,5,4,2], 3, 1]
print("d: ", d)
print("d[-3] :", d[-3])
print("d[-3][0] :", d[-3][0])
print("d[-3][-1] :", d[-3][-1])

print("e = d[-3]")
e = d[-3]
print(e)

z = a + b
print(z)
