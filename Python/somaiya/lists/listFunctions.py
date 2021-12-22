a = [1,3,5,7,9]

# Concatenation Of Lists: 
## Concatenation Of Lists: 
b = a + [2,4,6,8,10]

#  Appending On Lists: 
##  Appending On Lists: 
b.append(12)
print("b.append(12): ", b)

#  Extending Lists if appending more then one item we need to use extend: 
##  Extending Lists if appending more then one item we need to use extend: 
c = [1,2,3,4]
b.extend(c) 

# pop(), remove() and del() 
## pop(), remove() and del() 
print("a: ", a)
print("a.pop(): ", a.pop())
print("Updated a: ", a)

print("del a(0:3): ")
a.extend(c) 
a.extend(c) 
del a[0:3]
print("Updated a after del with slice: ", a)

print("a:", a);
print("a.remove(value which you want to delete: ") 
a.remove(1) 
print("a:", a);

# try:
#     b.append(12)
#   print("del a [0]: ", del a[0])
#   print("Updated a afer del: ", a)
# 
# catch(Exception e): 
#     print("Error: ",e)
