
import numpy as np
a = np.arange(25).reshape(5,5);
print(a);

print("\n######### Solution #########\n");
print(a[2:4,1:4])

print("\na[x1:x2, y1:y2]")
comment = """
Where,
    x1 is the starting index for row; 
    x2 is the ending index for row; 
    y1 is the starting index of column; 
    y2 is the starting index of column;
""";
print(comment);


print(a[:,-1]);
print(a[3,:]);
print("a[0:3,3]");
print(a[0:3,0:3]);

print("a[0:3,2]");
print(a[0:3,2]);


