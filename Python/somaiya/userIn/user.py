
a =[]; 
print("a: ", a)

for x in range(3):
    y = input("Enter anything: ");
    a.append(y);

print("a: ", a)

summer =0 
for x in a:
    summer += int(x);
    
print("sum: ", summer)
