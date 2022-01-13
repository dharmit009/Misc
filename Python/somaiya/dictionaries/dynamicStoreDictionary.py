
n = int(input("Enter total number of Cities: "))
my_dictionary = dict()

for x in range(0,n):
    ecity = str(input("Enter a city name: "))
    etemp = str(input("Enter temperature: "))
    my_dictionary[ecity] = etemp


for x, y in my_dictionary.items():
        print(x, ": ", y)
