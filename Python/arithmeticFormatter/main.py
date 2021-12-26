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

def formatter(data):
    tops = []
    operations = []
    bottoms = []
    splitter = []
    for x in data:
        splitter = x.split()
        tops.append(splitter[0])
        operations.append(splitter[-2])
        bottoms.append(splitter[-1])
    print("Splitter: ", splitter)
    print("Tops: ", tops)
    print("Operations: ", operations)
    print("Bottoms: ", bottoms)
    print("\n")

    for x in tops: 
        print("\t", x, end = "\t");
        for i, y in enumerate(bottoms): 
            print(operations[i], y)


        





    # if output == true: 
        


data = ['32 - 34', '25 + 45']
formatter(data)
