"""
write a  program in python to accept 5 integer elements from the list and swap 1st and last element

"""

a = list()
for x in range(5):
    i = int(input("Enter a number: "))
    a.append(i)


print("Before Swap: ...")
print("A: ", a)

temp = a[0]
a[0] = a[-1]
a[-1] = temp


print("After Swap: ...")
print("A: ", a)
