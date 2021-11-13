a=[1,2,3,8,9,4,7,1,0,2,3,99,4,7,1,0,2,9,7,8]; b = []; uniq = [];
for i in range(len(a)): 
    flag=0;
    if a[i] not in uniq:
        for j in range(len(a)): 
            if int(a[i])==int(a[j]):
                flag +=1; 
        if flag>=2: 
            uniq.append(a[i]);
        b.append(flag);

print(uniq);
