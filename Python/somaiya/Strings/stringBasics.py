a = "Hello World"
b = "This is \"sentence B\""
c = "lets see how a \t tab looks like" 
d = "lets see how a \"\r\" \r works like" 


print(a, b, c, sep='\n');
print(a[4]);
print(a.upper());
print(b.lower());
print(c.capitalize());
print("r is used for carriage return");
print(d);
print("Length of String A: ", len(a));

E = "Ashish"
s = 10000
print(type(s));

print("Employee Name: %s, Salary: %s" % (E,s));

## Error To Be Fixed: 
## Employee Name: %s, Salary: %s Ashish 10000
