# mess = """
#        _         _ _   _                    _   _      
#       / \   _ __(_) |_| |__  _ __ ___   ___| |_(_) ___ 
#      / _ \ | '__| | __| '_ \| '_ ` _ \ / _ \ __| |/ __|
#     / ___ \| |  | | |_| | | | | | | | |  __/ |_| | (__ 
#    /_/   \_\_|  |_|\__|_| |_|_| |_| |_|\___|\__|_|\___|
#                                                        
#     _____                          _   _            
#    |  ___|__  _ __ _ __ ___   __ _| |_| |_ ___ _ __ 
#    | |_ / _ \| '__| '_ ` _ \ / _` | __| __/ _ \ '__|
#    |  _| (_) | |  | | | | | | (_| | |_| ||  __/ |   
#    |_|  \___/|_|  |_| |_| |_|\__,_|\__|\__\___|_|   
#
# """

# print(mess)
def calculate(tops, bottoms, operations):
    result = list();
    for x,y,z in zip(tops, bottoms, operations):
        x = int(x)
        y = int(y)
        if z == '+':
            out = x + y; 
        elif z == "-":
            out = x - y;
        elif z == "*":
            out = x * y; 
        else:
            out = x // y; 
        result.append(out)
    
    return result;
        
# def funcChecker(data, operations, tops, bottoms):
#     if len(data) > 4:
#         print("Error: Too many problems.")
#         break;
#     elif '*' or '/' in operations:
#         print("Error: Operator must be '+' or '-'.")
#         break;
#     else: 
#         for x in bottoms:
#             if x > 9999:
#                 print("Error: Number cannot be greater than 4 Digits.")
#                 break;
#     

def formatter(data, output=False):
    print("")
    tops = []
    operations = []
    bottoms = []
    splitter = []
    for x in data:
        splitter = x.split()
        tops.append(splitter[0])
        operations.append(splitter[-2])
        bottoms.append(splitter[-1])
    funcChecker(data, operations, tops, bottoms);
    # print("Splitter: ", splitter)
    # print("Tops: ", tops)
    # print("Operations: ", operations)
    # print("Bottoms: ", bottoms)
    # print("\n")

    for x in tops:
        print("\t  ", x, end="\t", sep="")
    print("")
    for y,z in zip(operations, bottoms): 
        print("\t", y, " ", z, end="\t", sep="")
    print("")
    for _ in range(len(bottoms)):
         print("\t------\t", end="", sep="")   
    print("")

    result_of_operations = calculate(tops, bottoms, operations)

    if output == True:
        for out in result_of_operations:
            print("\t  ", out, end="\t", sep="")
        print("")

    print("")


data = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
formatter(data)
formatter(data, True)
