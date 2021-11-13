def test(): 
    print("Hello")
    return "World"; 

print(test()); 
print(type(test())); 

def a(*a): #args refered as *args
    for x in a: 
        print(x); 


def b(**b): #dictionary also refered as **kargs 
    for x in b:
        print("The var name is: ", x, " and its value is: ",b[x]); 



print("Function a"); 
a(23,2423,2342,242,234);
print("\n"); 
print("Function b"); 
b(a=76,b=890,c=123);
print("\n"); 
