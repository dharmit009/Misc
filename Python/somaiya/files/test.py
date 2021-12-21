numbers = [1,2,3,4,5,6,7,8,9,0];

for number in numbers: 
    print(number); 


fruit = 'Banana'
try:
    fruit[0] = 't'
except:
    print("Strings are not mutuable or editable"); 
    print("Therefore, fruit[0] = 't' generates an exception");
    
print(fruit);

