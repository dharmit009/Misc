myAge = 16

def runThisMethod(x,y):
    print("My name is", x, "I'm",y, "years old.\nHere are somethings I would like to give you")
    myGoods = ['apple', 'blueberries', 'cake', 10]
    i = 0 
    while i<len(myGoods):
        print(myGoods[i])
        i+=1



if __name__ == "__main__":
    try:
        print("Welcome to my program ...")
        myName='Carolina'
        myName[0] = 'K'
        myage = 10
            
    except:
        pass

    runThisMethod(myName, myAge)
