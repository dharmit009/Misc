# valid for driver or not ... 
#

age = int(input("Enter Your age:"));

if age >= 18: 
    print("You can apply for valid driving license."); 
else: 
    remain = 18 - age; 
    print("You will be able to apply after ", remain, "years"); 
