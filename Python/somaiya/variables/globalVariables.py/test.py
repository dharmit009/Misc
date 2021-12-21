mya = 5
def func1():
    mya = 50
def func2():
    global mya 
    mya = 50
def func3():
    print(mya);

func1()
func3()
print("After Global");
func2()
func3()

