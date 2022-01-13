def menu(name, *arguments, **keywords):
    if '-h' in arguments:
        print(arguments);
        print("--help");
    else: 
        print("test");


menu("name", '-a', '-b', '-c', '-h')
menu("name", '-a', '-b', '-c', '-r')
