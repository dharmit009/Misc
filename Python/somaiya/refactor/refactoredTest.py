
def runThisMethod(x,y):
    print("My name is", x, "I'm",y, "years old.")
    print("Here are somethings I would like to give you: ", end="")
    my_goods = ['apple', 'blueberries', 'cake', 10]
    for x in my_goods:
        print(x, end=", ")
    print("")


if __name__ == "__main__":
    print("Welcome to my program ...")
    my_name='Carolina'
    my_age = 10
    runThisMethod(my_name, my_age)
