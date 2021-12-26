"""
WAP to accept 10 numbers in the list and separate positive and negative number from the list

"""

a = []
pos = []
neg = list()

for x in range(11):
    i = int(input("Enter a Number: "))
    a.append(i)

print("A: ", a)


for x in a:
    if x>=0:
        pos.append(x);
    else:
        neg.append(x);


print("Positive Numbers: ", pos)
print("Negative Numbers: ", neg)
