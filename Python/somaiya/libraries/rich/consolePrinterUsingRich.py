from rich.console import Console
from rich.console import inspect
c = Console();

def difference(message): 
    print("Normal Print: ", message);
    c.print("Rich Print: ", message);
    print("");


message = "The main difference between normal print and rich print function it is that rich will automatically word-wrap the text according to terminal size.";

print("Check the difference!!\n");
difference(message);

print("Emoji Support: ");
message=":heart:";
difference(message);

message=":vampire:";
difference(message);

message=":brain:";
difference(message);

print("Automatic Highlighting of functions !!");
message="int a = random.randint()";
difference(message);

c.print("**CSS Like Styling:** ");
print("Hello", "World! has no such inbuilt attributes.");
c.print("Hello", "World! using attributes such style=\"bold red\".", style="bold red");
print("")

c.print("Grained Level Styling: ");
message='When there is a [bold cyan]Will[/bold cyan] there [u]is[/u] a [i]way[/i].'
difference(message)

list_a = [1,2,3,4,5]
print(list_a);
inspect(list_a, methods=True);















