a = list();
i = 0; 

while i<=5:
    n = int(input("Enter a number: "))
    a.append(n);
    i = i + 1;

print("A: ", a)
a.reverse()
p = list()
p = a
print("Reverse Format: ", p)
