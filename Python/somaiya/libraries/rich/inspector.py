from rich import inspect

my_list = ["foo", "bar"]
message = "test run "
print("Python's Way: \n" , dir(my_list))
print("\nRich's Way: ")
# TO show all methods
# inspect(my_list, all=True)

inspect(my_list, methods=True)
inspect(message, methods=True)
