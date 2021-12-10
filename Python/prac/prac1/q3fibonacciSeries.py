################################################################################################
# 1                                         0                                                  #
# 2                                        1 1                                                 #
# 3                                       1 2 1                                                #
# 4                                      1 3 3 1                                               #
# 5                                     1 4 6 4 1                                              #
# 6                                   1 5 10 10 5 1                                            #
################################################################################################

# * FIBONACCI:* Fibonacci series is a series of previous two numbers in the series. It always starts
# with zero and one. 

def fibonacci(n): 
    n0, n1 = 0, 1 
    out = 0

    if n < 0: 
        print("Error: Enter number greater then 0!"); 
    else: 
        for _ in range(0,n):
            n0 = n1
            n1 = out
            out = n0 + n1
            # 0 1 1 2 3 5
        return out


print("\t### Fibonacci Series ###\t");
n = int(input("Enter a number: "));
print(fibonacci(n))


