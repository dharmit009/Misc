def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)

    for arg in arguments:
        print(arg)
    print("-" * 40)

    for kw in keywords:
        print(kw, ":", keywords[kw])


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")


def basic(a, *arguments, **keywords):
    b = arguments;
    c = keywords;
    print(a);
    print("");
    print("Type Of Arguemnts: " , type(b));
    print("argument: ", b);
    print("");

    print("");
    print("Keywords", c);
    print("Type Of Keywords: " , type(c));
    print("");

basic("is this basic?", "yes i think so this must be arguments", "and all this must also be arguments", shop="Alaska", client="Me");
