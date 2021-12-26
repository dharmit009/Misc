"""Q3. write a program in python to display the elements of the list thrice if it is number and display the element
terminated with ‘#’ if it is not a number."""

a = [6,4,6,5,'a','b',3, 4.3]
print("a: ", a)

for x in a:
    if type(x) == int: 
        print(x,x,x)
    else : 
        print(str(x)+"#")

    
