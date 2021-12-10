import pandas as pd

def nl(): 
    print("");

a = pd.Series(["Test", 3,3.2]);
print(a);
print(type(a));
nl();

b = pd.Series(["Akshat", "America", "Ankit", "Arrow"]);
b.name="NPAT";
b.index["Name", "Place", "Animal", "Thing"]; 

print("B = ");
print(b);
print(type(b));
nl();

print("Values of B: ");
print(b.Values());
nl();

print("Values of B: ");
print(b.Values());
nl();

