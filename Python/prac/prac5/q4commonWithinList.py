"""Write the program to find at least one common  element from the list."""

a = [1,2,3,8,4,0,1,2,4,8,0,2] 
b = [31,2,23,8,14,0,11,2,14,8,0,2] 
uniqList = list()

print("A: ", a)
print("B: ", b)

for x in a:
    for y in b:
        if x == y:
            uniqList.append(x);

print("Common Elements: ", set(uniqList))

"""
Alternative Method: 

a = [1,2,0,3,4,8,1,2,3]
uniqList = list()

for x in a:
    if x not in uniqList:
        uniqList.append(x);

print(uniqList)

"""
