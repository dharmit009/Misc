def arraySorter(a): 
    for x in range(len(a)): 
        for y in range(len(a)): 
            if a[x]<a[y]:
                a[x],a[y]=a[y],a[x]; 
    return a; 


a = [1,2,4,-5,7,9,3,2]; 
out = arraySorter(a); 
print(out);
