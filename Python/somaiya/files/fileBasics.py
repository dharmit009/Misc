fname = input("Enter a filename: "); 
try: 
    fhandler = open(fname); 
except: 
    print("[E]: File cannot be opened: ", fname);
    quit(); 

count = 0
for i, line in enumerate(fhandler, start=1): 
    print(i, line, end=""); 
    count += 1; 

print("There are total ", count, "lines"); 
