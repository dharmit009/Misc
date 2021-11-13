import numpy as np

print("3x3:");
x = np.array([[1]*3,[1]*3])
print(x); 
print("\n");

print("Ones Like:");
x = np.arange(4, dtype=int);
print(np.ones_like(x)); 
print("\n");

print("Identity Matrix:");
print(np.identity(5)); 
