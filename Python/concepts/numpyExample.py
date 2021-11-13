import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([8, 3, 4, 9, 2, 7, 5])

# print("Data Type of Array a: ",type(a));
# print("Data Type of Array a: ",a.dtype);

c = np.array([1, 2, 3, 4, 5, 6, 1, 2, 3, 7, 8, 9])
# print(mul_a);

d = np.array([[[1, 2, 3], [4, 5, 6], [0, 0, -1]],
             [[-1, -2, -3], [4, 5, 6], [0, 0, 1]]])
# print(mul_b);

print(d[0, 1, 1])
print(d[1, 1, 2])
