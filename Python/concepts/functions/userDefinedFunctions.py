def greet(filename='test', username='test'):
    print(" ### ", filename, " ### ");
    print(" Hello,", username, "!");
    print("");
    return;


## variable length argument: 
def greet(name, mobile, *extra):
    print("Name:", name);
    print("Mobile:", mobile);
    print("extra:", extra);
    print("");
    
    for x in len(range(extra)): 
        print("Extra Argument [", x, "]: ", extra[x]);

    return;


greet('functions', 'nobody')
greet('functions',  785747, 'somethingExtra')
greet('functions',  785747, 'somethingExtra1','somethingExtra2')

