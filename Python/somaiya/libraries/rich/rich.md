# What is Rich Library ? 

Rich is a Python library for rich text and beautiful formatting in the terminal.

The Rich API makes it easy to add color and style to terminal output. Rich can also render pretty tables, progress bars, markdown, syntax highlighted source code, tracebacks, and more — out of the box.

## Installation:

`python -m pip install rich`
`pip3 install rich`

## Basic Usage: 

**Sample Code:**

```
from rich import print
print("Hello, [bold magenta]World[/bold magenta]!", ":vampire:", locals())

```

**Output:** 

```
Hello, World! 🧛
{
    '__name__': '__main__',
    '__doc__': None,
    '__package__': None,
    '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7f3316165420>,
    '__spec__': None,
    '__annotations__': {},
    '__builtins__': <module 'builtins' (built-in)>,
    '__file__': '/home/hmm/learning/Python/somaiya/libraries/rich/sample.py',
    '__cached__': None,
    'print': <function print at 0x7f33160d1870>
}
```

To use more features of rich library it is recommend to create a console object especially for terminal applications. 

```
from rich.console import Console
c = Console()
print("Check the difference: The main difference between normal print and rich print function it is that rich will automatically word-wrap the text according to terminal size.")
print("Hello, World!")
c.print("Check the difference: The main difference between normal print and rich print function it is that rich will automatically word-wrap the text according to terminal size.")
c.print("Hello, World!")

```
As you might expect, this will print "Hello World!" to the terminal. Note that unlike the builtin print function, Rich will word-wrap your text to fit within the terminal width










