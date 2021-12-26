
a = [1,2,0,3,4,8,1,2,3]
uniqList = list()
print("A: ",a)

for x in a:
    if x not in uniqList:
        uniqList.append(x);

print("Uniq: ", uniqList)

