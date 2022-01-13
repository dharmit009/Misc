
base_line = "Once upon a time, There lived a "

ad = list();
for i in range(0,3):
    print("Adjective[{}] ".format(i), end="", sep="");
    userin=str(input("Enter a adjective: "))
    ad.append(userin)

location = input("Enter a place name: ")
something = input("Enter something you like to do: ")

out = base_line + ad[0] + f"in the mountains of {location}, He used to like {something} everyday. But once day someone kicked him out. So he started {ad[2]} and {ad[1]}"
print(out)
