def displayDictionaries(A, B):
    print("")
    print("A: ", A);
    print("B: ", B);
    print("")

A = {1: 1, 2: 2, 3: 3, 4: 4};
B = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60};

displayDictionaries(A, B);
print("Let us update Dictionary A with the help of B.")
A.update(B)
displayDictionaries(A, B);

print("Keys: ", end="")
for key in A.keys():
    print(key, sep="", end=", ");

print("\nValues: ", end="")
for value in A.values():
    print(value, sep="", end=", ");

print("")
for x,y in A.items():
    print("Key: ", x, ", Items: ", y);
