
def display_histogram(myData):
    for key, value in myData.items():
        print("|Name:", key,"\t| Value:", value, "|", end="\t\t")
        for x in range(value):
            print("*", end="")
        print("")
    print("")


a = dict(
    Apple = 0,
    Avacado = 5, 
    Green = 2, 
    Banana = 3, 
    Grapes = 4, 
)

print("Displaying Histogram A: ")
display_histogram(a)

b = a.copy();
b["Apple"] = 5; 
b["Kiwi"] = 9; 

print("Displaying Histogram B: ")
display_histogram(b)


