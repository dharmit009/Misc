counts = dict()

names = ['a', 'b', 'c', 'd', 'a', 'b', 'd', 'd', 'c', 'd']
print("Names: ", names);

for x in names:
    if x not in counts:
        counts[x] = 1
    else:
        counts[x] = counts[x] + 1

print("Counts: ", counts)
print("")

print("The get() method ...")

print("Count of 'a': ", counts.get('a'))
print("Count of 'z': ", counts.get('z', 0)) # if not found then return 0 by default.
print("")
