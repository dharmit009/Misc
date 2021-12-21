# A dictionary is made up of 2 things they are:
# 1. Key.
# 2. Values.
#
# Here is a basic syntax for dictionary ... 

def disDict(a):
    print("The following Dictionary contains: \n", a, sep="");


a = {
        "Apple" : "GREEDY",
        "Green Apple" : "Green",
        "Pineapple" : "Yellow",
}

disDict(a);
print(a.get("Apple", "Yellow"))

# COMPLETED: dictionary constructor form 
c = dict(a='apple', b='banana',)
disDict(c);

# Dictionary Methods: 
print("Before clearing the dictionary: ")
disDict(a);
temp = a.copy();
a.clear()
print("After clearing the dictionary: ")
disDict(a);
# The copy method worked as expected .
disDict(temp);

# let us copy back the dictionary ...
a = temp.copy()
print("After copying the dictionary: ")
disDict(a);

print("\nLet us print all the keys of the dictionary ...");
print(a.keys());

print("""\nAnother thing to notice is the type of list this is ...
which is dictionary """);
print("Type a.keys() = " , type(a.keys()));

